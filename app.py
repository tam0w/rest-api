import json

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/send', methods=['GET','POST'])
def send():
    print(request.json)
    data = request.json
    return jsonify({'message': data['message']})

@app.route('/api/match', methods=['GET','POST'])
def send():
    global data
    print(data)
    return jsonify(data)

data = json.loads("""{'all_round_data': [[['Jett', 'Phoenix', 8, 'team', 'Kill'],
                     ['Omen', 'Jett', 43, 'team', 'Kill'],
                     ['Omen', 'Phoenix', 47, 'opponent', 'Spike'],
                     ['Jett', 'Omen', 54, 'team', 'Kill'],
                     ['Phoenix', 'Sova', 60, 'team', 'Kill'],
                     ['Jett', 'Killjoy', 66, 'team', 'Kill'],
                     ['Jett', 'Jett', 72, 'team', 'Spike']],
                    [['Omen', 'Phoenix', 4, 'team', 'Kill'],
                     ['Jett', 'Jett', 5, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 15, 'opponent', 'Kill'],
                     ['Sova', 'Killjoy', 21, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 21, 'opponent', 'Kill'],
                     ['Sova', 'Omen', 25, 'opponent', 'Kill'],
                     ['Phoenix', 'Omen', 25, 'team', 'Kill'],
                     ['Phoenix', 'Sova', 62, 'team', 'Kill']],
                    [['Jett', 'Phoenix', 8, 'team', 'Kill'],
                     ['Jett', 'Omen', 16, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 17, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 25, 'team', 'Kill'],
                     ['Sova', 'Killjoy', 26, 'opponent', 'Kill'],
                     ['Sova', 'Sova', 40, 'opponent', 'Kill'],
                     ['Omen', 'Killjoy', 68, 'team', 'Kill'],
                     ['Sova', 'Omen', 76, 'opponent', 'Kill'],
                     ['Sova', 'Jett', 91, 'opponent', 'Spike'],
                     ['Sova', 'Phoenix', 93, 'opponent', 'Kill']],
                    [['Phoenix', 'Killjoy', 15, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 18, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 30, 'opponent', 'Kill'],
                     ['Omen', 'Sova', 30, 'opponent', 'Spike'],
                     ['Phoenix', 'Omen', 31, 'opponent', 'Kill'],
                     ['Sova', 'Phoenix', 34, 'team', 'Kill'],
                     ['Jett', 'Sova', 38, 'opponent', 'Kill']],
                    [['Killjoy', 'Killjoy', 15, 'team', 'Kill'],
                     ['Omen', 'Omen', 23, 'opponent', 'Spike'],
                     ['Omen', 'Jett', 40, 'opponent', 'Kill'],
                     ['Jett', 'Sova', 41, 'opponent', 'Kill'],
                     ['Killjoy', 'Omen', 42, 'team', 'Kill'],
                     ['Jett', 'Omen', 44, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 51, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 52, 'team', 'Kill'],
                     ['Phoenix', 'Sova', 54, 'team', 'Kill'],
                     ['Killjoy', 'Phoenix', 65, 'team', 'Spike']],
                    [['Phoenix', 'Sova', 20, 'opponent', 'Kill'],
                     ['Omen', 'Phoenix', 21, 'team', 'Kill'],
                     ['Killjoy', 'Killjoy', 25, 'team', 'Kill'],
                     ['Killjoy', 'Omen', 30, 'team', 'Kill'],
                     ['Sova', 'Killjoy', 33, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 37, 'team', 'Kill'],
                     ['Sova', 'Jett', 47, 'opponent', 'Kill'],
                     ['Sova', 'Omen', 59, 'opponent', 'Kill'],
                     ['Sova', 'Jett', 78, 'opponent', 'Spike'],
                     ['Phoenix', 'Sova', 100, 'team', 'Kill'],
                     ['Phoenix', 'Phoenix', 113, 'team', 'Spike']],
                    [['Killjoy', 'Sova', 20, 'team', 'Kill'],
                     ['Omen', 'Jett', 21, 'opponent', 'Kill'],
                     ['Omen', 'Phoenix', 57, 'team', 'Kill'],
                     ['Omen', 'Jett', 59, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 81, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 95, 'opponent', 'Spike'],
                     ['Sova', 'Killjoy', 100, 'team', 'Kill'],
                     ['Sova', 'Omen', 109, 'team', 'Kill'],
                     ['Phoenix', 'Jett', 117, 'team', 'Spike']],
                    [['Killjoy', 'Jett', 8, 'team', 'Kill'],
                     ['Phoenix', 'Killjoy', 8, 'opponent', 'Kill'],
                     ['Sova', 'Omen', 22, 'team', 'Kill'],
                     ['Killjoy', 'Sova', 31, 'opponent', 'Kill'],
                     ['Killjoy', 'Phoenix', 32, 'opponent', 'Kill'],
                     ['Omen', 'Killjoy', 35, 'team', 'Kill'],
                     ['Jett', 'Sova', 36, 'team', 'Kill'],
                     ['Phoenix', 'Omen', 37, 'opponent', 'Kill'],
                     ['Phoenix', 'Jett', 61, 'opponent', 'Spike'],
                     ['Phoenix', 'Jett', 98, 'opponent', 'Kill']],
                    [['Jett', 'Phoenix', 23, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 25, 'opponent', 'Kill'],
                     ['Killjoy', 'Killjoy', 30, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 32, 'team', 'Kill'],
                     ['Phoenix', 'Killjoy', 34, 'team', 'Kill'],
                     ['Phoenix', 'Sova', 53, 'team', 'Kill'],
                     ['Omen', 'Phoenix', 71, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 81, 'opponent', 'Spike'],
                     ['Omen', 'Omen', 94, 'team', 'Kill'],
                     ['Omen', 'Phoenix', 111, 'team', 'Spike']],
                    [['Sova', 'Phoenix', 6, 'team', 'Kill'],
                     ['Sova', 'Sova', 8, 'team', 'Kill'],
                     ['Omen', 'Sova', 14, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 20, 'opponent', 'Kill'],
                     ['Phoenix', 'Killjoy', 28, 'team', 'Kill'],
                     ['Omen', 'Jett', 37, 'opponent', 'Spike'],
                     ['Omen', 'Omen', 50, 'team', 'Kill'],
                     ['Phoenix', 'Jett', 51, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 67, 'team', 'Spike']],
                    [['Phoenix', 'Phoenix', 13, 'opponent', 'Kill'],
                     ['Jett', 'Omen', 15, 'team', 'Kill'],
                     ['Phoenix', 'Jett', 18, 'opponent', 'Kill'],
                     ['Killjoy', 'Phoenix', 25, 'team', 'Kill'],
                     ['Jett', 'Killjoy', 30, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 37, 'team', 'Kill'],
                     ['Omen', 'Sova', 50, 'team', 'Kill'],
                     ['Killjoy', 'Omen', 54, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 73, 'opponent', 'Spike'],
                     ['Killjoy', 'Sova', 91, 'opponent', 'Kill']],
                    [['Jett', 'Phoenix', 5, 'team', 'Kill'],
                     ['Jett', 'Killjoy', 7, 'team', 'Kill'],
                     ['Sova', 'Sova', 9, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 9, 'opponent', 'Kill'],
                     ['Phoenix', 'Jett', 18, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 23, 'opponent', 'Kill'],
                     ['Omen', 'Sova', 34, 'team', 'Kill'],
                     ['Omen', 'Jett', 42, 'opponent', 'Spike'],
                     ['Omen', 'Omen', 47, 'team', 'Kill'],
                     ['Omen', 'Phoenix', 57, 'team', 'Spike']],
                    [['Phoenix', 'Killjoy', 11, 'opponent', 'Kill'],
                     ['Phoenix', 'Sova', 12, 'opponent', 'Kill'],
                     ['Jett', 'Jett', 13, 'opponent', 'Kill'],
                     ['Phoenix', 'Omen', 22, 'opponent', 'Kill'],
                     ['Sova', 'Phoenix', 35, 'opponent', 'Kill']],
                    [['Sova', 'Jett', 8, 'opponent', 'Kill'],
                     ['Killjoy', 'Sova', 9, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 20, 'team', 'Kill'],
                     ['Sova', 'Phoenix', 23, 'opponent', 'Kill'],
                     ['Killjoy', 'Killjoy', 24, 'opponent', 'Kill'],
                     ['Omen', 'Killjoy', 25, 'team', 'Kill'],
                     ['Sova', 'Omen', 27, 'opponent', 'Kill']],
                    [['Phoenix', 'Phoenix', 18, 'opponent', 'Kill'],
                     ['Sova', 'Phoenix', 19, 'team', 'Kill'],
                     ['Jett', 'Sova', 21, 'opponent', 'Kill'],
                     ['Jett', 'Jett', 24, 'team', 'Kill'],
                     ['Omen', 'Jett', 24, 'opponent', 'Kill'],
                     ['Killjoy', 'Omen', 39, 'opponent', 'Kill'],
                     ['Killjoy', 'Killjoy', 62, 'opponent', 'Kill']],
                    [['Jett', 'Killjoy', 13, 'team', 'Kill'],
                     ['Jett', 'Jett', 14, 'opponent', 'Kill'],
                     ['Killjoy', 'Phoenix', 29, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 37, 'opponent', 'Kill'],
                     ['Sova', 'Omen', 51, 'opponent', 'Kill'],
                     ['Jett', 'Phoenix', 51, 'opponent', 'Kill'],
                     ['Jett', 'Sova', 56, 'opponent', 'Kill']],
                    [['Omen', 'Omen', 2, 'team', 'Kill'],
                     ['Sova', 'Sova', 4, 'opponent', 'Kill'],
                     ['Phoenix', 'Sova', 6, 'team', 'Kill'],
                     ['Jett', 'Jett', 7, 'opponent', 'Kill'],
                     ['Omen', 'Phoenix', 15, 'team', 'Kill'],
                     ['Jett', 'Killjoy', 17, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 19, 'team', 'Kill'],
                     ['Omen', 'Jett', 33, 'team', 'Spike'],
                     ['Phoenix', 'Killjoy', 38, 'team', 'Kill']],
                    [['Omen', 'Jett', 4, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 14, 'team', 'Kill'],
                     ['Killjoy', 'Killjoy', 17, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 24, 'team', 'Kill'],
                     ['Omen', 'Phoenix', 26, 'opponent', 'Kill'],
                     ['Killjoy', 'Sova', 39, 'opponent', 'Kill'],
                     ['Sova', 'Omen', 77, 'opponent', 'Kill']],
                    [['Phoenix', 'Phoenix', 9, 'team', 'Kill'],
                     ['Phoenix', 'Jett', 15, 'team', 'Kill'],
                     ['Killjoy', 'Omen', 24, 'team', 'Kill'],
                     ['Omen', 'Sova', 25, 'team', 'Spike'],
                     ['Sova', 'Sova', 33, 'opponent', 'Kill'],
                     ['Sova', 'Killjoy', 34, 'opponent', 'Kill'],
                     ['Killjoy', 'Jett', 43, 'opponent', 'Kill'],
                     ['Omen', 'Sova', 43, 'team', 'Kill'],
                     ['Phoenix', 'Killjoy', 52, 'team', 'Kill']],
                    [['Sova', 'Omen', 13, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 19, 'team', 'Kill'],
                     ['Killjoy', 'Sova', 24, 'opponent', 'Kill'],
                     ['Jett', 'Sova', 25, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 26, 'opponent', 'Kill'],
                     ['Phoenix', 'Killjoy', 30, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 31, 'opponent', 'Kill'],
                     ['Jett', 'Phoenix', 34, 'opponent', 'Kill']],
                    [['Killjoy', 'Killjoy', 17, 'team', 'Kill'],
                     ['Omen', 'Killjoy', 29, 'opponent', 'Kill'],
                     ['Jett', 'Phoenix', 31, 'team', 'Kill'],
                     ['Omen', 'Sova', 37, 'opponent', 'Kill'],
                     ['Omen', 'Jett', 46, 'team', 'Kill'],
                     ['Omen', 'Jett', 46, 'opponent', 'Kill'],
                     ['Omen', 'Sova', 47, 'team', 'Kill'],
                     ['Omen', 'Omen', 48, 'opponent', 'Kill'],
                     ['Phoenix', 'Jett', 68, 'team', 'Spike'],
                     ['Omen', 'Phoenix', 97, 'opponent', 'Kill'],
                     ['Omen', 'Phoenix', 107, 'opponent', 'Spike']],
                    [['Jett', 'Omen', 7, 'opponent', 'Kill'],
                     ['Jett', 'Omen', 16, 'team', 'Kill'],
                     ['Phoenix', 'Sova', 21, 'opponent', 'Kill'],
                     ['Jett', 'Sova', 26, 'team', 'Kill'],
                     ['Killjoy', 'Jett', 28, 'opponent', 'Kill'],
                     ['Phoenix', 'Killjoy', 32, 'opponent', 'Kill'],
                     ['Jett', 'Phoenix', 48, 'opponent', 'Kill']],
                    [['Jett', 'Sova', 9, 'opponent', 'Kill'],
                     ['Phoenix', 'Omen', 12, 'opponent', 'Kill'],
                     ['Omen', 'Killjoy', 14, 'opponent', 'Kill'],
                     ['Phoenix', 'Phoenix', 17, 'opponent', 'Kill'],
                     ['Phoenix', 'Jett', 26, 'opponent', 'Kill']]],
 'anchor_times': [47,
                  0,
                  91,
                  30,
                  23,
                  78,
                  95,
                  61,
                  81,
                  37,
                  73,
                  42,
                  0,
                  0,
                  0,
                  0,
                  33,
                  0,
                  25,
                  0,
                  68,
                  0,
                  0],
 'assists': [['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '1', '0', '0', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
             ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '2', '0', '0', '0', '0', '0'],
             ['1', '1', '0', '1', '0', '0', '0', '0', '1', '1'],
             ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '1', '0', '0', '2', '1', '1', '0', '0', '0'],
             ['0', '0', '0', '1', '0', '0', '0', '0', '0', '1'],
             ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
             ['0', '2', '0', '1', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '1', '0', '0', '0', '0', '0', '0', '1', '0'],
             ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
             ['1', '0', '1', '0', '1', '1', '0', '1', '1', '0'],
             ['1', '0', '0', '0', '1', '1', '1', '0', '1', '0'],
             ['0', '0', '0', '0', '1', '1', '0', '1', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0']],
 'awp_info': ['none',
              'none',
              'none',
              'none',
              'team',
              'team',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'none',
              'opponent',
              'opponent'],
 'bombsites': ['C',
               'False',
               'False',
               'C',
               'C',
               'A',
               'B',
               'A',
               'C',
               'C',
               'A',
               'A',
               'False',
               'False',
               'False',
               'False',
               'False',
               'False',
               'A',
               'False',
               'False',
               'False',
               'False'],
 'buy_info_oppo': ['700',
                   '500',
                   '4,300',
                   '3,900',
                   '4,700',
                   '400',
                   '000',
                   '1900',
                   ',800',
                   '2,300',
                   '4,000',
                   '1900',
                   '700',
                   '3,000',
                   '600',
                   '4,600',
                   '4,600',
                   ',800',
                   '4,500',
                   '1900',
                   '4,500',
                   '4,700',
                   '4,800'],
 'buy_info_team': ['700',
                   '2,700',
                   '3,600',
                   '1,900',
                   '4,400',
                   '4,300',
                   '4,100',
                   '4,300',
                   '3,200',
                   '4,300',
                   '4,000',
                   '4,300',
                   '700',
                   '600',
                   '4,100',
                   '900',
                   '4,500',
                   '4,100',
                   '2,000',
                   '4,500',
                   '3,700',
                   '3,300',
                   '2,800'],
 'defuses': [True,
             False,
             False,
             False,
             True,
             True,
             True,
             False,
             True,
             True,
             False,
             True,
             False,
             False,
             False,
             False,
             False,
             False,
             False,
             False,
             True,
             False,
             False],
 'dt_players': ['1611',
                '1611',
                '1611',
                'tam0w',
                'TR GSTREAM',
                'frenchShooter',
                'LFT teJaz',
                'lynX',
                '1611',
                '1611',
                'MrCoolone YT',
                '1611',
                'tam0w',
                'hfMe1',
                'MrCoolone YT',
                'TR GSTREAM',
                'Grayyish',
                'hfMe1',
                '1611',
                'cav',
                'TR GSTREAM',
                'cav',
                'frenchShooter'],
 'dt_string': '31/12/2023',
 'fb_team': ['team',
             'team',
             'team',
             'opponent',
             'team',
             'opponent',
             'team',
             'team',
             'team',
             'team',
             'opponent',
             'team',
             'opponent',
             'opponent',
             'opponent',
             'team',
             'team',
             'opponent',
             'team',
             'opponent',
             'team',
             'opponent',
             'opponent'],
 'fbs_players': ['hfMe1',
                 'cav',
                 'hfMe1',
                 '1611',
                 'tam0w',
                 '1611',
                 'tam0w',
                 'tam0w',
                 'hfMe1',
                 'frenchShooter',
                 '1611',
                 'hfMe1',
                 '1611',
                 'LFT teJaz',
                 '1611',
                 'hfMe1',
                 'cav',
                 'Grayyish',
                 'MrCoolone YT',
                 'LFT teJaz',
                 'tam0w',
                 'lynX',
                 'lynX'],
 'first_action_times': [[8, 43, 47, 54, 60, 66, 72],
                        [4, 5, 15, 21, 21, 25, 25, 62],
                        [8, 16, 17, 25, 26, 40, 68, 76, 91, 93],
                        [15, 18, 30, 30, 31, 34, 38],
                        [15, 23, 40, 41, 42, 44, 51, 52, 54, 65],
                        [20, 21, 25, 30, 33, 37, 47, 59, 78, 100, 113],
                        [20, 21, 57, 59, 81, 95, 100, 109, 117],
                        [8, 8, 22, 31, 32, 35, 36, 37, 61, 98],
                        [23, 25, 30, 32, 34, 53, 71, 81, 94, 111],
                        [6, 8, 14, 20, 28, 37, 50, 51, 67],
                        [13, 15, 18, 25, 30, 37, 50, 54, 73, 91],
                        [5, 7, 9, 9, 18, 23, 34, 42, 47, 57],
                        [11, 12, 13, 22, 35],
                        [8, 9, 20, 23, 24, 25, 27],
                        [18, 19, 21, 24, 24, 39, 62],
                        [13, 14, 29, 37, 51, 51, 56],
                        [2, 4, 6, 7, 15, 17, 19, 33, 38],
                        [4, 14, 17, 24, 26, 39, 77],
                        [9, 15, 24, 25, 33, 34, 43, 43, 52],
                        [13, 19, 24, 25, 26, 30, 31, 34],
                        [17, 29, 31, 37, 46, 46, 47, 48, 68, 97, 107],
                        [7, 16, 21, 26, 28, 32, 48],
                        [9, 12, 14, 17, 26]],
 'first_is_plant': [False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False],
 'first_kill_times': [8,
                      4,
                      8,
                      15,
                      15,
                      20,
                      20,
                      8,
                      23,
                      6,
                      13,
                      5,
                      11,
                      8,
                      18,
                      13,
                      2,
                      4,
                      9,
                      13,
                      17,
                      7,
                      9],
 'fk_death': ['Phoenix',
              'Phoenix',
              'Phoenix',
              'Killjoy',
              'Killjoy',
              'Sova',
              'Sova',
              'Jett',
              'Phoenix',
              'Phoenix',
              'Phoenix',
              'Phoenix',
              'Killjoy',
              'Jett',
              'Phoenix',
              'Killjoy',
              'Omen',
              'Jett',
              'Phoenix',
              'Omen',
              'Killjoy',
              'Omen',
              'Sova'],
 'fk_player': ['Jett',
               'Omen',
               'Jett',
               'Phoenix',
               'Killjoy',
               'Phoenix',
               'Killjoy',
               'Killjoy',
               'Jett',
               'Sova',
               'Phoenix',
               'Jett',
               'Phoenix',
               'Sova',
               'Phoenix',
               'Jett',
               'Omen',
               'Omen',
               'Phoenix',
               'Sova',
               'Killjoy',
               'Jett',
               'Jett'],
 'fscore': '10-13',
 'kills': [['1', '1', '3', '0', '0', '0', '0', '0', '0', '0'],
           ['1', '2', '1', '0', '1', '1', '1', '0', '1', '0'],
           ['1', '0', '2', '1', '0', '4', '1', '0', '0', '0'],
           ['0', '0', '0', '0', '1', '0', '1', '1', '0', '3'],
           ['0', '2', '0', '3', '0', '0', '0', '2', '1', '0'],
           ['2', '1', '0', '2', '0', '3', '0', '0', '0', '1'],
           ['2', '0', '0', '1', '2', '0', '0', '0', '2', '0'],
           ['1', '0', '1', '1', '1', '0', '2', '0', '0', '3'],
           ['2', '2', '1', '0', '0', '0', '2', '0', '1', '0'],
           ['1', '2', '0', '0', '2', '0', '1', '0', '1', '0'],
           ['2', '0', '1', '1', '0', '0', '2', '1', '0', '2'],
           ['2', '1', '2', '0', '0', '1', '0', '0', '2', '0'],
           ['0', '0', '0', '0', '0', '1', '0', '1', '0', '3'],
           ['1', '1', '0', '0', '0', '3', '2', '0', '0', '0'],
           ['0', '0', '1', '0', '1', '0', '2', '1', '1', '1'],
           ['0', '0', '1', '1', '0', '1', '0', '3', '1', '0'],
           ['3', '2', '0', '0', '0', '1', '0', '2', '0', '0'],
           ['0', '1', '0', '1', '0', '1', '2', '0', '2', '0'],
           ['1', '3', '0', '1', '0', '2', '1', '0', '0', '0'],
           ['0', '2', '1', '0', '0', '1', '2', '1', '1', '0'],
           ['2', '0', '1', '1', '0', '0', '0', '0', '5', '0'],
           ['0', '0', '2', '0', '0', '0', '1', '2', '0', '2'],
           ['0', '0', '0', '0', '0', '0', '0', '1', '1', '3']],
 'kills_opp': [0,
               3,
               5,
               5,
               3,
               4,
               2,
               5,
               3,
               2,
               5,
               3,
               5,
               5,
               5,
               5,
               3,
               5,
               3,
               5,
               5,
               5,
               5],
 'kills_team': [5,
                5,
                4,
                1,
                5,
                5,
                5,
                4,
                5,
                5,
                4,
                5,
                0,
                2,
                2,
                2,
                5,
                2,
                5,
                3,
                4,
                2,
                0],
 'map_name': 'Haven',
 'outcomes': ['win',
              'win',
              'loss',
              'loss',
              'win',
              'win',
              'win',
              'loss',
              'win',
              'win',
              'loss',
              'win',
              'loss',
              'loss',
              'loss',
              'loss',
              'win',
              'loss',
              'win',
              'loss',
              'loss',
              'loss',
              'loss'],
 'plants': [True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            False,
            False,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
            False],
 'players_agents': '{"cav": "Omen", "MrCoolone YT": "Phoenix", "hfMe1": '
                   '"Jett", "tam0w": "Killjoy", "frenchShooter": "Sova", "LFT '
                   'teJaz": "Sova", "TR GSTREAM": "Killjoy", "lynX": "Jett", '
                   '"Grayyish": "Omen", "1611": "Phoenix"}',
 'rounds': 23,
 'scoreboard': [['MrCoolone YT', '20', '14', '9', 'team'],
                ['cav', '22', '16', '4', 'team'],
                ['hfMe1', '17', '22', '1', 'team'],
                ['tam0w', '13', '20', '5', 'team'],
                ['frenchShooter', '8', '19', '9', 'team']],
 'sides': ['Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Defense',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack',
           'Attack'],
 'true_fb': [True,
             True,
             False,
             True,
             True,
             False,
             True,
             False,
             False,
             True,
             True,
             True,
             True,
             True,
             False,
             False,
             True,
             True,
             True,
             False,
             False,
             True,
             True]}""")


if __name__ == '__main__':
    app.run()
