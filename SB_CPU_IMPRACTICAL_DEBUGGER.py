import SB_tools
import csv

#辞書
with open('dic/notype.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    notype_words = list(reader)

def get_my_word():
    #頭文字の入手
    #「「？」からはじまることば」を取得
    initial = SB_tools.get_driver().execute_script('return document.getElementById("input")').get_attribute("placeholder")[1]
    ene_word = SB_tools.get_ene_word()
    ene_HP = SB_tools.get_ene_HP()
    ene_defence_power = SB_tools.get_ene_defence_power()
    my_attack_power = SB_tools.get_my_attack_power()


    #即死できたら出力(どのCPUもつけるべき)
    if(SB_tools.get_change_ability_limit() >= 1):max_damage,word,necesary_ability = SB_tools.get_max_damage(ene_word,my_attack_power,ene_defence_power,ransuu=0.85)
    else:max_damage,word,necesary_ability = SB_tools.get_max_damage_no_ability_change(ene_word,my_attack_power,ene_defence_power,ransuu=0.85)
    if(max_damage >= ene_HP and word not in SB_tools.get_used_words()):
        
        SB_tools.change_ability(necesary_ability)
        return word

    if(SB_tools.get_my_ability() != "デバッガー"):SB_tools.change_ability("デバッガー")

    for i in notype_words:
        word = i[0]

        if(word[0] == initial):
            return word
        
    print("詰み")
    return None
