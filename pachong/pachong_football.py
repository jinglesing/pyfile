from urllib2 import urlopen
import urlparse
import bs4

BASE_URL = "http://soccerdata.sports.qq.com"
PLAYER_LIST_QUERY = "/playerSearch.aspx?lega=%s&pn=%d"
league = ['epl', 'seri', 'bund', 'liga', 'fran', 'scot', 'holl', 'belg']
page_number_limit = 100
player_fields = ['league_cn', 'img', 'name_cn', 'name', 'team', 'age', 'position_cn', 'nation', 'birth', 'query', 'id',
                 'teamid', 'league']


def get_player_match(url):
    html = urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "lxml")
    matches = [dd for dd in soup.select('.shtdm tr') if dd.contents[1].name != 'th']
    records = []
    for item in [dd for dd in matches if len(dd.contents) > 11]:  ## filter out the personal part
        record = []
        for match in [dd for dd in item.contents if type(dd) is bs4.element.Tag]:
            if match.string:
                record.append(match.string)
            else:
                for d in [dd for dd in match.contents if type(dd) is bs4.element.Tag]:
                    query = dict([(k, v[0]) for k, v in urlparse.parse_qs(d['href']).items()])
                    record.append('teamid' in query and query['teamid'] or query['id'])
                    record.append(d.string and d.string or 'na')
        records.append(record)
    return records[1:]  ##remove the first record as the header


def get_players_match(playerlist, baseurl=BASE_URL + '/player.aspx?'):
    result = []
    for item in playerlist:
        url = baseurl + item[10]
        print url
        result = result + get_player_match(url)
    return result


match_fields = ['date_cn', 'homeid', 'homename_cn', 'matchid', 'score', 'awayid', 'awayname_cn', 'league_cn',
                'firstteam', 'playtime', 'goal', 'assist', 'shoot', 'run', 'corner', 'offside', 'foul', 'violation',
                'yellowcard', 'redcard', 'save']
write_csv('m.csv', get_players_match(result), match_fields)