

def is_first_blood_induce_win(match_info):
    if 'radiant_win' not in match_info:
        return None
    elif match_info['objectives'] == None:
        return None
    else:
        win_camp = 'radiant' if match_info['radiant_win'] is True else 'dire'
        for objects in match_info['objectives']:
            if objects['type'] == 'CHAT_MESSAGE_FIRSTBLOOD':
                player_slot = objects['player_slot']
                break
        for player in match_info['players']:
            if player['player_slot'] == player_slot:
                first_blood_camp = 'radiant' if player['isRadiant'] is True else 'dire'
        if win_camp == first_blood_camp:
            return True
        else:
            return False



