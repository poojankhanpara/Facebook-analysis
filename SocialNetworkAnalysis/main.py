import fbconsole
import requests
import pprint
import matplotlib.pyplot as plt
import networkx as nx
if __name__ == '__main__':
    pass
fbconsole.AUTH_SCOPE = ['publish_actions', 'read_stream',
                            'user_actions.news', 'publish_stream',
                            'publish_checkins', 'email',
                            'user_status','read_mailbox',
                            'friends_online_presence','xmpp_login',
                            'read_stream','read_friendlists'
                           ]
fbconsole.authenticate()
#fbconsole.ACCESS_TOKEN='CAACEdEose0cBAKFZBe9tgS38XgFZAbGuvutlD8UB9df604Vo9FZCnAkgI6ZCNm4n76D2Xbc6xyNRUM0VmvdZBw8SjL5TZAZCBixktVlDiFbduZCvQ1CddZAvEmNrjfiqfMAkSSF8b8Gf9rc9znowK0ZBZA1PUZBZBk4vGHeD8DBnJpqZBMmCjhc2bi6YHA6QTpHmMroms5P5CKAy7ZCHlsjPp4Gg1FwF2jltGvWA8gZD'
base_wall_url = 'https://graph.facebook.com/me/friends?access_token='
wall_url = base_wall_url + fbconsole.ACCESS_TOKEN
print(wall_url)
response = requests.get(wall_url)
print ('response:',response)
dictFriends = response.json()
pprint.pprint(dictFriends) # prints the json dictionary

g=nx.DiGraph()
g.is_directed()
g.add_node('Poojan')

nodes_friends_list={}
nodes_friends_list[0]='Poojan'
i=1
for d in dictFriends['data']:
    name = d['name']
    g.add_node(name)
    g.add_edge('Poojan', name)
    nodes_friends_list[i]=name
    i+=1
pprint.pprint(nodes_friends_list)
pprint.pprint(g.nodes())
pprint.pprint(len(nodes_friends_list))
pprint.pprint(len(g.nodes()))
nx.draw(g,with_labels=True)
#nx.draw_networkx(g,nodes_friends_list)
plt.savefig("path.png")
plt.show()
plt.savefig("path.png")