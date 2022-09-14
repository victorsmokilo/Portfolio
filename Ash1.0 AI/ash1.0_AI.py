# -*- coding: utf-8 -*-

class effectivty_lists:
    def __init__(self,
                flying_strong,
                flying_weak,
                flying_null,
                ground_strong,
                ground_weak,
                ground_null,
                water_strong,
                water_weak,
                water_null,
                fire_strong,
                fire_weak,
                fire_null,
                grass_strong,
                grass_weak,
                grass_null,
                electric_strong,
                electric_weak,
                electric_null,
                rock_strong,
                rock_weak,
                rock_null,
                fighting_strong,
                fighting_weak,
                fighting_null,
                dragon_strong,
                dragon_weak,
                dragon_null,
                dark_strong,
                dark_weak,
                dark_null,
                fairy_strong,
                fairy_weak,
                fairy_null,
                psychic_strong,
                psychic_weak,
                psychic_null,
                poison_strong,
                poison_weak,
                poison_null,
                steel_strong,
                steel_weak,
                steel_null,
                ghost_strong,
                ghost_weak,
                ghost_null,
                bug_strong,
                bug_weak,
                bug_null,
                ice_strong,
                ice_weak,
                ice_null,
                normal_strong,
                normal_weak,
                normal_null):
                    self.flying_strong = flying_strong
                    self.flying_weak = flying_weak
                    self.flying_null = flying_null
                    self.ground_strong = ground_strong
                    self.ground_weak = ground_weak
                    self.ground_null = ground_null
                    self.water_strong = water_strong
                    self.water_weak = water_weak
                    self.water_null = water_null
                    self.fire_weak = fire_weak
                    self.fire_null = fire_null
                    self.fire_strong = fire_strong
                    self.grass_weak = grass_weak
                    self.grass_null = grass_null
                    self.grass_strong = grass_strong
                    self.electric_weak = electric_weak
                    self.electric_strong = electric_strong
                    self.electric_null = electric_null
                    self.rock_null = rock_null
                    self.rock_strong = rock_strong
                    self.rock_weak = rock_weak
                    self.fighting_null = fighting_null
                    self.fighting_strong = fighting_strong
                    self.fighting_weak = fighting_weak
                    self.dragon_strong = dragon_strong
                    self.dragon_weak = dragon_weak
                    self.dragon_null = dragon_null
                    self.dark_strong = dark_strong
                    self.dark_weak = dark_weak
                    self.dark_null = dark_null
                    self.fairy_strong = fairy_strong
                    self.fairy_weak = fairy_weak
                    self.fairy_null = fairy_null
                    self.psychic_weak = psychic_weak
                    self.psychic_null = psychic_null
                    self.psychic_strong = psychic_strong
                    self.poison_weak = poison_weak
                    self.poison_null = poison_null
                    self.poison_strong = poison_strong
                    self.steel_weak = steel_weak
                    self.steel_strong = steel_strong
                    self.steel_null = steel_null
                    self.ghost_null = ghost_null
                    self.ghost_strong = ghost_null
                    self.ghost_weak = ghost_weak
                    self.bug_null = bug_null
                    self.bug_strong = bug_strong
                    self.bug_weak = bug_weak
                    self.ice_strong = ice_strong
                    self.ice_weak = ice_weak
                    self.ice_null = ice_null
                    self.normal_strong = normal_strong
                    self.normal_weak = normal_weak
                    self.normal_null = normal_null


effectives = effectivty_lists(['fighting','bug','grass'], #flying
                              ['rock','steel','electric'],
                              [],
                              ['poison','rock','steel','fire','electric'], #ground
                              ['bug','grass'],
                              ['flying'],
                              ['ground','rock','fire'], #water
                              ['water','grass','dragon'],
                              [],
                              ['bug','steel','grass','ice'], #fire
                              ['rock','fire','water','dragon'],
                              [],
                              ['ground','rock','water'],#grass
                              ['flying','poison','bug','steel','fire','grass','dragon'],
                              [],
                              ['flying','water'],#electric
                              ['grass','electric','dragon'],
                              ['ground'],
                              ['flying','bug','fire','ice'],#rock
                              ['fighting','ground','steel'],
                              [],
                              ['normal','rock','steel','ice','dark'],#fighting
                              ['flying','poison','bug','psychic','fairy'],
                              ['ghost'],
                              ['dragon'],#dragon
                              ['steel'],
                              ['fairy'],
                              ['ghost','psychic'],#dark
                              ['fighting','dark','fairy'],
                              [],
                              ['fighting','dragon','dark'],#fairy
                              ['poison','steel','fire'],
                              [],
                              ['fighting','poison'],#psychic
                              ['steel','psychic'],
                              ['dark'],
                              ['grass','fairy'],#poison
                              ['poison','ground','rock','ghost'],
                              ['steel'],
                              ['rock','ice','fairy'],#steel
                              ['steel','fire','water','electric'],
                              [],
                              ['ghost','psychic'],#ghost
                              ['dark'],
                              ['normal'],
                              ['grass','psychic','dark'],#bug
                              ['fighting','flying','poison','ghost','steel','fire','fairy'],
                              [],
                              ['flying','ground','grass','dragon'],#ice
                              ['steel','fire','water','ice'],
                              [],
                              [],#normal
                              ['rock','steel'],
                              ['ghost'],
                              )







#TARGET RETURNS------------------------------------------------------------------------------------------------------

def return_targets(move, user):
    
    #for CPU
    user._priority = int(move_priority_dict[move])
    targets = [] 
    if user == simulated_field._first_computer or user == simulated_field._second_computer:
        if move_targets_dict[move] == 'single_attack':
            if simulated_field._first_user._health > 0:
                targets.append(simulated_field._first_user)
            if simulated_field._second_user._health > 0:
                targets.append(simulated_field._second_user)
            targets = [targets[random.randrange(0,len(targets))]]
            return targets
        if move_targets_dict[move] == 'double_attack':
            return [simulated_field._first_user,simulated_field._second_user]
        if move_targets_dict[move] == 'field_attack':
            if user == simulated_field._first_computer:
                return [simulated_field._first_user,simulated_field._second_user, simulated_field._second_computer]
            if user == simulated_field._second_computer:
                return [simulated_field._first_user,simulated_field._second_user, simulated_field._first_computer]
        if move_targets_dict[move] == 'double_enhancement':
            return [simulated_field._first_computer,simulated_field._second_computer]
        if move_targets_dict[move] == 'single_enhancement':
            return [user]
        if move_targets_dict[move] == 'choice_enhancement':
            if simulated_field._first_computer._health > 0:
                targets.append(simulated_field._first_computer)
            if simulated_field._second_computer._health > 0:
                targets.append(simulated_field._second_computer)
            targets = [targets[random.randrange(0,len(targets))]]
            return targets
            
    
    #for user
    if user == simulated_field._first_user or user == simulated_field._second_user:
        if move_targets_dict[move] == 'single_attack':
            if simulated_field._first_computer._health > 0:
                targets.append(simulated_field._first_computer)
            if simulated_field._second_computer._health > 0:
                targets.append(simulated_field._second_computer)
            targets = [targets[random.randrange(0,len(targets))]]
            return targets
        if move_targets_dict[move] == 'double_attack':
            return [simulated_field._first_computer,simulated_field._second_computer]
        if move_targets_dict[move] == 'field_attack':
            if user == simulated_field._first_user:
                return [simulated_field._first_computer,simulated_field._second_computer, simulated_field._second_user]
            if user == simulated_field._second_user:
                return [simulated_field._first_computer,simulated_field._second_computer, simulated_field._first_user]
        if move_targets_dict[move] == 'double_enhancement':
            return [simulated_field._first_user,simulated_field._second_user]
        if move_targets_dict[move] == 'single_enhancement':
            return [user]
        if move_targets_dict[move] == 'choice_enhancement':
            if simulated_field._first_user._health > 0:
                targets.append(simulated_field._first_user)
            if simulated_field._second_user._health > 0:
                targets.append(simulated_field._second_user)
            targets = [targets[random.randrange(0,len(targets))]]
            return targets
        
        
        
        
def return_targets_main(move, user, u1, u2, o1, o2, opponent):
    
    #for CPU
    
    targets = [] 
    real_targets = []
    if user == simulated_field._first_computer or simulated_field._second_computer:
        if move_targets_dict[move] == 'single_attack':
            if simulated_field._first_user._health > 0:
                targets.append(simulated_field._first_user)
                real_targets.append(u1)
            if simulated_field._second_user._health > 0:
                targets.append(simulated_field._second_user)
                real_targets.append(u2)
            chooser = random.randrange(0,len(targets))
            targets = [[targets[chooser]], [real_targets[chooser]]]
            return targets
        
        
        
        
        if move_targets_dict[move] == 'double_attack':
            return [[simulated_field._first_user,simulated_field._second_user],[u1,u2]]
        
        
        if move_targets_dict[move] == 'field_attack':
            if user == simulated_field._first_computer:
                return [[simulated_field._first_user,simulated_field._second_user, simulated_field._second_computer],[u1,u2,o2]]
            if user == simulated_field._second_computer:
                return [[simulated_field._first_user,simulated_field._second_user, simulated_field._first_computer],[u1,u2,o1]]
            
            
        if move_targets_dict[move] == 'double_enhancement':
            return [[simulated_field._first_computer,simulated_field._second_computer],[o1,o2]]
        
        
        
        if move_targets_dict[move] == 'single_enhancement':
            
            return [[user],[opponent]]
        
        
        if move_targets_dict[move] == 'choice_enhancement':
            if simulated_field._first_computer._health > 0:
                targets.append(simulated_field._first_computer)
                real_targets.append(o1)
            if simulated_field._second_computer._health > 0:
                targets.append(simulated_field._second_computer)
                real_targets.append(o2)
            chooser = random.randrange(0,len(targets))
            targets = [[targets[chooser]],[real_targets[chooser]]]
            return targets        
        
        
        
#---------------------------------------------------------------------------

def checkstatuses_sim():
    if team_1_config_sim._aquaring == True:
        team_1_config_sim._aquaringcount -= 1
        targets = []
        targets.append(simulated_field._first_user)
        targets.append(simulated_field._second_user)
        for b in range(len(targets)):
            try:
                if targets[b]._condition == 'alive' and targets[b]._health != targets[b]._orighealth and targets[b]._heatlh >= 0:
                    heal_sim(targets[b], round(targets[b]._orighealth/10))
            except:
                pass
        if team_1_config_sim._aquaringcount == 0:
            team_1_config._aquaring = False
            
    if team_2_config_sim._aquaring == True:
        team_2_config_sim._aquaringcount -= 1
        targets = []
        targets.append(simulated_field._first_computer)
        targets.append(simulated_field._second_computer)
        for b in range(len(targets)):
            try:
                if targets[b]._condition == 'alive' and targets[b]._health != targets[b]._orighealth and targets[b]._heatlh >= 0:
                    heal_sim(targets[b], round(targets[b]._orighealth/10))
            except:
                pass
        if team_2_config_sim._aquaringcount == 0:
            team_2_config._aquaring = False
            
            
            
    if team1clouds_sim[0] > 0:
        
        targets = []
        targets = []
        targets.append(simulated_field._first_user)
        targets.append(simulated_field._second_user)
        for b in range(len(targets)):
            try:
                if targets[b]._condition == 'alive' and targets[b]._health != targets[b]._orighealth and targets[b]._heatlh >= 0:
                    heal_sim(targets[b], round(targets[b]._orighealth/100) * 8 * team1clouds_sim[0])
            except:
                pass
            
            
            
    if team2clouds_sim[0] > 0:
        
        targets = []
        targets = []
        targets.append(simulated_field._first_computer)
        targets.append(simulated_field._second_computer)
        for b in range(len(targets)):
            try:
                if targets[b]._condition == 'alive' and targets[b]._health != targets[b]._orighealth and targets[b]._heatlh >= 0:
                    heal_sim(targets[b], round(targets[b]._orighealth/100) * 8 * team2clouds_sim[0])
            except:
                pass
            
    
    
    pokemon = [simulated_field._first_computer, simulated_field._second_computer, simulated_field._first_user, simulated_field._second_user]
    for i in range(len(pokemon)):
        if pokemon[i]._status == 'poisoned' and pokemon[i]._condition == 'alive':
            damage = round(pokemon[i]._poisoncount * pokemon[i]._orighealth * 1/16)
            if damage > pokemon[i]._health:
                damage = pokemon[i]._health
            pokemon[i]._health -= damage
            
            checkhealth_sim()
            
        if pokemon[i]._status == 'burned' and pokemon[i]._condition == 'alive':
            damage = round(pokemon[i]._orighealth * 1/8)
            if damage > pokemon[i]._health:
                damage = pokemon[i]._health
            pokemon[i]._health -= damage
            
            
        try:
            if pokemon[i]._perish == True and pokemon[i]._perishcount == 0 and pokemon[i]._condition == 'alive':
                pokemon[i]._health -= pokemon[i]._health
            elif pokemon[i]._perish == True and pokemon[i]._perishcount == 1 and pokemon[i]._condition == 'alive':
                pokemon[i]._perishcount -= 1
                
            elif pokemon[i]._perish == True and pokemon[i]._perishcount > 1 and pokemon[i]._condition == 'alive':
                pokemon[i]._perishcount -= 1
        except:
            pass
        
        
                
        if pokemon[i]._cursed == True and pokemon[i]._condition == 'alive' and pokemon[i]._health > 0:
            damage = round((pokemon[i]._orighealth * 1/4) + 0.5)
            if damage > pokemon[i]._health:
                damage = pokemon[i]._health
                
                pokemon[i]._health -= damage
    
    checkhealth_sim()
     

      
    if currentfield_sim._userstickyweb == True:
        if currentfield_sim._userstickyweb_count == 8:
            currentfield_sim._userstickyweb = False
        else:
            currentfield._userstickyweb_count += 1
            
    if currentfield_sim._opponentstickyweb == True:
        if currentfield_sim._opponentstickyweb_count == 8:
            currentfield_sim._opponentstickyweb = False
        else:
            currentfield_sim._opponentstickyweb_count += 1

    if currentfield_sim._status == 'raining':
        if currentfield_sim._raincount == 0:
            currentfield_sim._rain = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._raincount -= 1
            for i in range(len(pokemon)):
                 if (pokemon[i]._element == 'water' or  pokemon[i]._element2 == 'water') and pokemon[i]._condition == 'alive':
                    if pokemon[i]._health != pokemon[i]._orighealth:
                        heal_ammount = round(pokemon[i]._orighealth * 1/12)
                        if heal_ammount > pokemon[i]._health:
                            heal_ammount = pokemon[i]._health
                        heal_sim(pokemon[i], heal_ammount)
            
            
    if currentfield_sim._usermist == True:
        if currentfield_sim._usermist_count == 3:
            currentfield_sim._usermist = False
        else:
            currentfield_sim._usermist_count += 1
            
            
    if currentfield_sim._opponentmist == True:
        if currentfield_sim._opponentmist_count == 3:
            currentfield_sim._opponentmist = False
        else:
            currentfield_sim._opponentmist_count += 1
           
            
    if currentfield_sim._status == 'downpour':
        if currentfield_sim._raincount == 0:
            currentfield_sim._rain = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._raincount -= 1
            for i in range(len(pokemon)):
                 if (pokemon[i]._element == 'water' or  pokemon[i]._element2 == 'water') and pokemon[i]._condition == 'alive':
                    if pokemon[i]._health != pokemon[i]._orighealth:
                        heal_ammount = round(pokemon[i]._orighealth * 1/8)
                        if heal_ammount > pokemon[i]._health:
                            heal_ammount = pokemon[i]._health
                            heal_sim(pokemon[i], heal_ammount)
        

    if currentfield_sim._status == 'hailing':
        if currentfield_sim._hailcount == 0:
            currentfield_sim._hailing = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._hailcount -= 1
            for i in range(len(pokemon)):
                if pokemon[i]._condition == 'alive' and pokemon[i]._element != 'ice' and pokemon[i]._element2 != 'ice':
                    damage = round(pokemon[i]._orighealth * 1/16)
                    if damage > pokemon[i]._health:
                        damage = pokemon[i]._health
                    pokemon[i]._health -= damage
                    
                    
    if currentfield_sim._status == 'blizzard':
        if currentfield_sim._hailcount == 0:
            currentfield_sim._hailing = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._hailcount -= 1
            for i in range(len(pokemon)):
                if pokemon[i]._condition == 'alive' and pokemon[i]._element != 'ice' and pokemon[i]._element2 != 'ice':
                    damage = round(pokemon[i]._orighealth * 1/10)
                    if damage > pokemon[i]._health:
                        damage = pokemon[i]._health
                    pokemon[i]._health -= damage
                    
                    
    if currentfield_sim._status == 'sandstorm':
        if currentfield_sim._sand_stormcount == 0:
            currentfield_sim._sand_storm = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._sand_stormcount -= 1
            for i in range(len(pokemon)):
                if pokemon[i]._condition == 'alive' and ((pokemon[i]._element != 'ground' and pokemon[i]._element2 != 'ground') and (pokemon[i]._element != 'rock' and pokemon[i]._element2 != 'rock') and (pokemon[i]._element != 'steel' and pokemon[i]._element2 != 'steel')):
                    damage = round(pokemon[i]._orighealth * 1/16)
                    if damage > pokemon[i]._health:
                        damage = pokemon[i]._health
                    pokemon[i]._health -= damage
                    
                    
    if currentfield_sim._status == 'grassy_terrain':
        if currentfield_sim._grasscount == 0:
            currentfield_sim._grass = False
            currentfield_sim._status = 'normal'
        else:
            currentfield_sim._grasscount -= 1
        
        
    checkhealth_sim()
    
    
    for i in range(len(pokemon)):
        if 'accelerated' in pokemon[i]._abilities and pokemon[i]._condition == 'alive':
            buf_spd_sim(pokemon[i],5)
            
        if 'regenerating' in pokemon[i]._abilities and pokemon[i]._condition == 'alive':
            health = round(pokemon[i]._orighealth * 0.15)
            if pokemon[i]._health != pokemon[i]._orighealth:
                heal_sim(pokemon[i], health)
                
                
        if 'regenerator' in pokemon[i]._abilities and pokemon[i]._condition == 'alive':
            if pokemon[i] == simulated_field._first_computer:
                ally = simulated_field._second_computer
            if pokemon[i] == simulated_field._second_computer:
                ally = simulated_field._first_computer
            if pokemon[i] == simulated_field._first_user:
                ally = simulated_field._second_user
            if pokemon[i] == simulated_field._second_user:
                ally = simulated_field._first_user
            health = round(ally._orighealth * 0.15)
            if ally._health != ally._orighealth and ally._condition == 'alive':
                heal_sim(pokemon[i], health)
                
                

def can_user_select_move_sim(pokemon):
    if pokemon._recharge == False and pokemon._chargeup_solar == False and pokemon._chargeup_meteor == False and pokemon._last_move != 'rollout':
        return True
    else:
        return False


def can_user_move_sim(pokemon):
    if pokemon._health <= 0:
        return False
    
    try:
        if pokemon._status == 'sleeping':
            if pokemon._sleepcount < 1:
                pokemon._status = 'normal'
            else:
                pokemon._sleepcount -= random.randrange(0,4)
                return False
    except:
        pass
    
    
    try:
        if pokemon._status == 'paralyzed':
            if random.randrange(0,5) == 1:
                return False
    except:
        pass
    
    try:
        if pokemon._status == 'frozen':
            if random.randrange(0,5) != 1:
                return False
            else:
                pokemon._status = 'normal'
    except:
        pass
    
    return True
    
                
def choose_random_move_sim(pokemon):
    possible_moves = [pokemon._move1, pokemon._move2, pokemon._move3, pokemon._move4]
    x = random.randrange(0,4)
    return possible_moves[x]





# BATTLE SIMULATIONS ----------------------------------------------------------------------------------------------------------------------------


def trainer_move_choice(u1, u2, o1, o2, ut, ot, opponent, total_sims, user_number):
    
    move1_totals = []
    move2_totals = []
    move3_totals = []
    move4_totals = []
    move5_totals = []

    
    #using first move--------------------------------------------------------------------------------------------------------------------------------
    
    for i in range(total_sims):
        
        human1, human2, main_computer, computer2, user_team, opponent_team = copy.deepcopy(u1), copy.deepcopy(u2), copy.deepcopy(opponent), copy.deepcopy(o2), copy.deepcopy(ut), copy.deepcopy(ot)
        
        currentfield_sim._rain = currentfield._rain
        currentfield_sim._hailing = currentfield._hailing
        currentfield_sim._sand_storm = currentfield._sand_storm
        currentfield_sim._grass = currentfield._grass
        currentfield_sim._raincount = currentfield._raincount
        currentfield_sim._hailcount = currentfield._hailcount
        currentfield_sim._sand_stormcount = currentfield._sand_stormcount
        currentfield_sim._grasscount = currentfield._grasscount
        currentfield_sim._background = currentfield._background
        currentfield_sim._status = currentfield._status
        currentfield_sim._trickroom = currentfield._trickroom
        currentfield_sim._trickroomcount = currentfield._trickroomcount
        currentfield_sim._opponentstickyweb = currentfield._opponentstickyweb
        currentfield_sim._userstickyweb = currentfield._userstickyweb
        currentfield_sim._opponentspikes = currentfield._opponentspikes
        currentfield_sim._userspikes = currentfield._userspikes
        currentfield_sim._opponentpoisonspikes = currentfield._opponentpoisonspikes
        currentfield_sim._userpoisonspikes = currentfield._userpoisonspikes
        currentfield_sim._usermist = currentfield._usermist
        currentfield_sim._opponentmist = currentfield._opponentmist
        

        team_1_config_sim._wish1_active = team_1_config._wish1_active
        team_1_config_sim._wish2_active = team_1_config._wish2_active
        team_2_config_sim._wish1_active = team_2_config._wish1_active
        team_2_config_sim._wish2_active = team_2_config._wish2_active
        
        team_1_config_sim._aquaring = team_1_config._aquaring
        team_1_config_sim._aquaringcount = team_1_config._aquaringcount
        team_2_config_sim._aquaring = team_2_config._aquaring
        team_2_config_sim._aquaringcount = team_2_config._aquaringcount
        

        
        
        
        simulated_field._first_user = human1
        simulated_field._second_user = human2
        simulated_field._first_computer = main_computer
        simulated_field._second_computer = computer2
        
        
        
        team1clouds_sim[0] = team1clouds[0]
        team2clouds_sim[0] = team2clouds[0]
        
        
        human1._move_selected, human1._targets = 'none','none'
        human2._move_selected, human2._targets = 'none','none'
        main_computer._move_selected, main_computer._targets = 'none','none'
        computer2._move_selected, computer2._targets = 'none','none'
        
        for k in range(len(user_team)):
            user_team[k]._move_selected, user_team[k]._targets = 'none','none'
        for k in range(len(opponent_team)):
            opponent_team[k]._move_selected, opponent_team[k]._targets = 'none','none'
            
       
        main_computer._move_selected = main_computer._move1
        
        all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
        
        first_targets = all_targets[0]
        
        real_targets = all_targets[1]
        
        main_computer._targets = first_targets
        
        first_attack = True
        
        
        
        
        for battle_round in range(5):
            
            user_total_health = 0
            user_total_health += simulated_field._first_user._health
            user_total_health += simulated_field._second_user._health
            for g in range(len(user_team)):
                user_total_health += user_team[g]._health
                
            computer_total_health = 0
            computer_total_health += simulated_field._first_computer._health
            computer_total_health += simulated_field._second_computer._health
            for g in range(len(opponent_team)):
                computer_total_health += user_team[g]._health
            
            if computer_total_health == 0 or user_total_health == 0:
                break
            
            
            
            
            if first_attack:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
                    
            else:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._first_computer._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
            
            if simulated_field._first_user._last_move == 'rollout':
                simulated_field._first_user._last_move = 'none'
                 
            if simulated_field._second_user._last_move == 'rollout':
                simulated_field._second_user._last_move = 'none'
                    
            if simulated_field._first_computer._last_move == 'rollout':
                simulated_field._first_computer._last_move = 'none'
                
            if simulated_field._second_computer._last_move == 'rollout':
                simulated_field._second_computer._last_move = 'none'
                 
            
            
            #assign moves
            
            if first_attack:
                
                if user_number == 2:
                    if first_opponent_simulation[0] == 'none':
        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                    elif first_opponent_simulation[0] == 'swap':
                        
                        x = copy.deepcopy(simulated_field._second_computer)
                        
                        for k in range(ot):
                            if ot[k] == new_opponent[0]:
                                y = copy.deepcopy(opponent_team[k])
                                index = k
                                
                        simulated_field._second_computer = y
                        opponent_team.remove(opponent_team[index])
                        opponent_team._append(x)
                        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                        
                        
                        
                    else:
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        computer2._move_selected = first_opponent_simulation[0][0]
                        computer2._targets = first_opponent_simulation[0][1]
                        
                        
                        first_attack = False
                        
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                    
                    
                else:  
                    if can_user_select_move_sim(human1):
                        human1._move_selected = choose_random_move_sim(human1)
                        human1._targets = return_targets(human1._move_selected, human1)
                        human1._can_move = True
                    else:
                        human1._can_move = False
                        
                    if can_user_select_move_sim(human2):
                        human2._move_selected = choose_random_move_sim(human2)
                        human2._targets = return_targets(human2._move_selected, human2)
                        human2._can_move = True
                    else:
                        human2._can_move = False
                        
                    if can_user_select_move_sim(computer2):
                        computer2._move_selected = choose_random_move_sim(computer2)
                        computer2._targets = return_targets(computer2._move_selected, computer2)
                        computer2._can_move = True
                    else:
                        computer2._can_move = False
                        
                    
                    first_attack = False
                
                    all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                
                
            else:
                        
                if can_user_select_move_sim(simulated_field._first_user):
                    simulated_field._first_user._move_selected = choose_random_move_sim(simulated_field._first_user)
                    simulated_field._first_user._targets = return_targets(simulated_field._first_user._move_selected, simulated_field._first_user)
                    simulated_field._first_user._can_move = True
                else:
                    simulated_field._first_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_user):
                    simulated_field._second_user._move_selected = choose_random_move_sim(simulated_field._second_user)
                    simulated_field._second_user._targets = return_targets(simulated_field._second_user._move_selected, simulated_field._second_user)
                    simulated_field._second_user._can_move = True
                else:
                    simulated_field._second_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_computer):
                    simulated_field._second_computer._move_selected = choose_random_move_sim(simulated_field._second_computer)
                    simulated_field._second_computer._targets = return_targets(simulated_field._second_computer._move_selected, simulated_field._second_computer)
                    simulated_field._second_computer._can_move = True
                else:
                    simulated_field._second_computer._can_move = False
                    
                if can_user_select_move_sim(simulated_field._first_computer):
                    simulated_field._first_computer._move_selected = choose_random_move_sim(simulated_field._first_computer)
                    simulated_field._first_computer._targets = return_targets(simulated_field._first_computer._move_selected, simulated_field._first_computer)
                    simulated_field._first_computer._can_move = True
                else:
                    simulated_field._first_computer._can_move = False
                
                
                
                all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
            
            
            #sorting by speed
            
            all_opponent_list.sort(key=lambda x: x._speed, reverse=True)
            
            
            if currentfield_sim._trickroom == True:
                all_opponent_list.sort(key=lambda x: x._speed, reverse=False)
            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
            
            
            for n in range(len(all_opponent_list)):
                try:
                    if all_opponent_list[n]._recharge == True:
                        all_opponent_list[n]._recharge = False
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'solar_beam_2'
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'meteor_beam_2'
                except:
                    pass
                
                
              
            if team_1_config_sim._wish1_active:
                if simulated_field._first_user._health > 0:
                    heal_sim(simulated_field._first_user._health, round(simulated_field._first_user._health/2))
                team_1_config_sim._wish1_active = False
                
            if team_1_config_sim._wish2_active:
                if simulated_field._second_user._health > 0:
                    heal_sim(simulated_field._second_user._health, round(simulated_field._second_user._health/2))
                team_1_config_sim._wish2_active = False
                
            if team_2_config_sim._wish1_active:
                if simulated_field._first_computer._health > 0:
                    heal_sim(simulated_field._first_computer._health, round(simulated_field._first_computer._health/2))
                team_2_config_sim._wish1_active = False
                
            if team_2_config_sim._wish2_active:
                if simulated_field._second_computer._health > 0:
                    heal_sim(simulated_field._second_computer._health, round(simulated_field._second_computer._health/2))
                team_2_config_sim._wish2_active = False
                
                
            
            
               
            
            for move_user in range(len(all_opponent_list)):
               if can_user_move_sim(all_opponent_list[move_user]):
                   
                   
                   if all_opponent_list[move_user]._condition == 'alive':
                        if all_opponent_list[move_user]._move_selected == 'instruct':
                            
                             if all_opponent_list[move_user] == simulated_field._first_user:
                                 ally = simulated_field._second_user
                             if all_opponent_list[move_user] == simulated_field._second_user:
                                 ally = simulated_field._first_user
                             if all_opponent_list[move_user] == simulated_field._first_computer:
                                 ally = simulated_field._second_computer
                             if all_opponent_list[move_user] == simulated_field._second_computer:
                                 ally = simulated_field._first_computer
                                
                             if ally._condition == 'alive' and ally._can_move and ally._recharge == False and ally._chargeup_solar == False and ally._chargeup_meteor == False and ally._last_move != 'instruct' and ally._last_move != 'mirror_move' and instruct_check(ally):
                                 eval(ally[move_user]._move_selected + '_sim')(ally[move_user], ally[move_user]._targets)
                                 
                        
                        elif all_opponent_list[move_user]._move_selected == 'quash':
                            all_opponent_list[move_user]._priority -= 10
                            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                        else:
                            eval(all_opponent_list[move_user]._move_selected + '_sim')(all_opponent_list[move_user], all_opponent_list[move_user]._targets)
                            all_opponent_list[move_user]._last_move = all_opponent_list[move_user]._move_selected
                            
                        checkhealth_sim()
            
                   

            
            checkstatuses_sim()        
            checkhealth_round_end_sim(user_team,opponent_team)
             
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        total_score = 0
        
        for j in range(len(user_team)):
            if ut[j]._health > 0:  
                total_score += round((((ut[j]._health - user_team[j]._health)*100)/ut[j]._health))
                
                
        for j in range(len(opponent_team)):
            if ot[j]._health > 0:
                total_score -= round((((ot[j]._health - opponent_team[j]._health)*100)/ot[j]._health))
        
                
        
        if u1._health > 0:
            total_score += round((((u1._health - human1._health)*100)/u1._health))
        
        
        if u2._health > 0:
            total_score += round((((u2._health - human2._health)*100)/u2._health))
        
        
        if o1._health > 0:
            total_score -= round((((o1._health - main_computer._health)*100)/o1._health))
        
        
        if o2._health > 0:
            total_score -= round((((o2._health - computer2._health)*100)/o2._health))
        
        
        move1_totals.append([total_score, real_targets])
        
        
    possible_targets = []
    possible_target_results = []
    
    for k in range(len(move1_totals)):
        if move1_totals[k][1] not in possible_targets:
            possible_targets.append(move1_totals[k][1])
            
    for k in range(len(possible_targets)):
        sim_score = 0
        sim_target_count = 0
        for j in range(len(move1_totals)):
            if possible_targets[k] == move1_totals[j][1]:
                sim_target_count += 1
                sim_score += move1_totals[j][0]
        sim_score = round(sim_score/sim_target_count)
        possible_target_results.append([sim_score,possible_targets[k]])
    
    
    maximum = 'none'
    max_score = -99999
    
    for k in range(len(possible_target_results)):
        if possible_target_results[k][0] > max_score:
            max_score = possible_target_results[k][0]
            maximum = possible_target_results[k][1]
            
            
    move1_totals = [max_score,maximum]  
        
        
        
    #using second move--------------------------------------------------------------------------------------------------------------------------------
    
    
    for i in range(total_sims):
        
        human1, human2, main_computer, computer2, user_team, opponent_team = copy.deepcopy(u1), copy.deepcopy(u2), copy.deepcopy(opponent), copy.deepcopy(o2), copy.deepcopy(ut), copy.deepcopy(ot)
        
        currentfield_sim._rain = currentfield._rain
        currentfield_sim._hailing = currentfield._hailing
        currentfield_sim._sand_storm = currentfield._sand_storm
        currentfield_sim._grass = currentfield._grass
        currentfield_sim._raincount = currentfield._raincount
        currentfield_sim._hailcount = currentfield._hailcount
        currentfield_sim._sand_stormcount = currentfield._sand_stormcount
        currentfield_sim._grasscount = currentfield._grasscount
        currentfield_sim._background = currentfield._background
        currentfield_sim._status = currentfield._status
        currentfield_sim._trickroom = currentfield._trickroom
        currentfield_sim._trickroomcount = currentfield._trickroomcount
        

        team_1_config_sim._wish1_active = team_1_config._wish1_active
        team_1_config_sim._wish2_active = team_1_config._wish2_active
        team_2_config_sim._wish1_active = team_2_config._wish1_active
        team_2_config_sim._wish2_active = team_2_config._wish2_active
        
        team_1_config_sim._aquaring = team_1_config._aquaring
        team_1_config_sim._aquaringcount = team_1_config._aquaringcount
        team_2_config_sim._aquaring = team_2_config._aquaring
        team_2_config_sim._aquaringcount = team_2_config._aquaringcount
        

        
        
        
        simulated_field._first_user = human1
        simulated_field._second_user = human2
        simulated_field._first_computer = main_computer
        simulated_field._second_computer = computer2
        
        
        
        team1clouds_sim[0] = team1clouds[0]
        team2clouds_sim[0] = team2clouds[0]
        
        
        human1._move_selected, human1._targets = 'none','none'
        human2._move_selected, human2._targets = 'none','none'
        main_computer._move_selected, main_computer._targets = 'none','none'
        computer2._move_selected, computer2._targets = 'none','none'
        
        for k in range(len(user_team)):
            user_team[k]._move_selected, user_team[k]._targets = 'none','none'
        for k in range(len(opponent_team)):
            opponent_team[k]._move_selected, opponent_team[k]._targets = 'none','none'
            
       
        main_computer._move_selected = main_computer._move2
        
        all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
        
        first_targets = all_targets[0]
        
        real_targets = all_targets[1]
        
        main_computer._targets = first_targets
        
        first_attack = True
        
        
        
        
        for battle_round in range(5):
            
            user_total_health = 0
            user_total_health += simulated_field._first_user._health
            user_total_health += simulated_field._second_user._health
            for g in range(len(user_team)):
                user_total_health += user_team[g]._health
                
            computer_total_health = 0
            computer_total_health += simulated_field._first_computer._health
            computer_total_health += simulated_field._second_computer._health
            for g in range(len(opponent_team)):
                computer_total_health += user_team[g]._health
            
            if computer_total_health == 0 or user_total_health == 0:
                break
            
            if first_attack:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
                    
            else:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._first_computer._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
            
            
            if simulated_field._first_user._last_move == 'rollout':
                simulated_field._first_user._last_move = 'none'
                 
            if simulated_field._second_user._last_move == 'rollout':
                simulated_field._second_user._last_move = 'none'
                    
            if simulated_field._first_computer._last_move == 'rollout':
                simulated_field._first_computer._last_move = 'none'
                
            if simulated_field._second_computer._last_move == 'rollout':
                simulated_field._second_computer._last_move = 'none'
                 
             
                        
            #assign moves
            
            if first_attack:
                
                if user_number == 2:
                    if first_opponent_simulation[0] == 'none':
        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                    elif first_opponent_simulation[0] == 'swap':
                        
                        x = copy.deepcopy(simulated_field._second_computer)
                        
                        for k in range(ot):
                            if ot[k] == new_opponent[0]:
                                y = copy.deepcopy(opponent_team[k])
                                index = k
                                
                        simulated_field._second_computer = y
                        opponent_team.remove(opponent_team[index])
                        opponent_team._append(x)
                        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                        
                        
                        
                    else:
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        computer2._move_selected = first_opponent_simulation[0][0]
                        computer2._targets = first_opponent_simulation[0][1]
                        
                        
                        first_attack = False
                        
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                    
                    
                else:  
                    if can_user_select_move_sim(human1):
                        human1._move_selected = choose_random_move_sim(human1)
                        human1._targets = return_targets(human1._move_selected, human1)
                        human1._can_move = True
                    else:
                        human1._can_move = False
                        
                    if can_user_select_move_sim(human2):
                        human2._move_selected = choose_random_move_sim(human2)
                        human2._targets = return_targets(human2._move_selected, human2)
                        human2._can_move = True
                    else:
                        human2._can_move = False
                        
                    if can_user_select_move_sim(computer2):
                        computer2._move_selected = choose_random_move_sim(computer2)
                        computer2._targets = return_targets(computer2._move_selected, computer2)
                        computer2._can_move = True
                    else:
                        computer2._can_move = False
                        
                    
                    first_attack = False
                
                    all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                
                
            else:
                        
                if can_user_select_move_sim(simulated_field._first_user):
                    simulated_field._first_user._move_selected = choose_random_move_sim(simulated_field._first_user)
                    simulated_field._first_user._targets = return_targets(simulated_field._first_user._move_selected, simulated_field._first_user)
                    simulated_field._first_user._can_move = True
                else:
                    simulated_field._first_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_user):
                    simulated_field._second_user._move_selected = choose_random_move_sim(simulated_field._second_user)
                    simulated_field._second_user._targets = return_targets(simulated_field._second_user._move_selected, simulated_field._second_user)
                    simulated_field._second_user._can_move = True
                else:
                    simulated_field._second_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_computer):
                    simulated_field._second_computer._move_selected = choose_random_move_sim(simulated_field._second_computer)
                    simulated_field._second_computer._targets = return_targets(simulated_field._second_computer._move_selected, simulated_field._second_computer)
                    simulated_field._second_computer._can_move = True
                else:
                    simulated_field._second_computer._can_move = False
                    
                if can_user_select_move_sim(simulated_field._first_computer):
                    simulated_field._first_computer._move_selected = choose_random_move_sim(simulated_field._first_computer)
                    simulated_field._first_computer._targets = return_targets(simulated_field._first_computer._move_selected, simulated_field._first_computer)
                    simulated_field._first_computer._can_move = True
                else:
                    simulated_field._first_computer._can_move = False
                
                
                
                all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
            
            
            #sorting by speed
            
            all_opponent_list.sort(key=lambda x: x._speed, reverse=True)
            
            
            if currentfield_sim._trickroom == True:
                all_opponent_list.sort(key=lambda x: x._speed, reverse=False)
            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
            
            
            for n in range(len(all_opponent_list)):
                try:
                    if all_opponent_list[n]._recharge == True:
                        all_opponent_list[n]._recharge = False
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'solar_beam_2'
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'meteor_beam_2'
                except:
                    pass
                
                
              
            if team_1_config_sim._wish1_active:
                if simulated_field._first_user._health > 0:
                    heal_sim(simulated_field._first_user._health, round(simulated_field._first_user._health/2))
                team_1_config_sim._wish1_active = False
                
            if team_1_config_sim._wish2_active:
                if simulated_field._second_user._health > 0:
                    heal_sim(simulated_field._second_user._health, round(simulated_field._second_user._health/2))
                team_1_config_sim._wish2_active = False
                
            if team_2_config_sim._wish1_active:
                if simulated_field._first_computer._health > 0:
                    heal_sim(simulated_field._first_computer._health, round(simulated_field._first_computer._health/2))
                team_2_config_sim._wish1_active = False
                
            if team_2_config_sim._wish2_active:
                if simulated_field._second_computer._health > 0:
                    heal_sim(simulated_field._second_computer._health, round(simulated_field._second_computer._health/2))
                team_2_config_sim._wish2_active = False
                
                
               
               
            
            for move_user in range(len(all_opponent_list)):
               if can_user_move_sim(all_opponent_list[move_user]):
                   
                   
                   if all_opponent_list[move_user]._condition == 'alive':
                        if all_opponent_list[move_user]._move_selected == 'instruct':
                            
                             if all_opponent_list[move_user] == simulated_field._first_user:
                                 ally = simulated_field._second_user
                             if all_opponent_list[move_user] == simulated_field._second_user:
                                 ally = simulated_field._first_user
                             if all_opponent_list[move_user] == simulated_field._first_computer:
                                 ally = simulated_field._second_computer
                             if all_opponent_list[move_user] == simulated_field._second_computer:
                                 ally = simulated_field._first_computer
                                
                             if ally._condition == 'alive' and ally._can_move and ally._recharge == False and ally._chargeup_solar == False and ally._chargeup_meteor == False and ally._last_move != 'instruct' and ally._last_move != 'mirror_move' and instruct_check(ally):
                                 eval(ally[move_user]._move_selected + '_sim')(ally[move_user], ally[move_user]._targets)
                                 
                        
                        elif all_opponent_list[move_user]._move_selected == 'quash':
                            all_opponent_list[move_user]._priority -= 10
                            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                        else:
                            eval(all_opponent_list[move_user]._move_selected + '_sim')(all_opponent_list[move_user], all_opponent_list[move_user]._targets)
                            all_opponent_list[move_user]._last_move = all_opponent_list[move_user]._move_selected
                            
                        checkhealth_sim()
                     
             
                    
             
            checkstatuses_sim()        
            checkhealth_round_end_sim(user_team,opponent_team)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        total_score = 0
        
        for j in range(len(user_team)):
            if ut[j]._health > 0:  
                total_score += round((((ut[j]._health - user_team[j]._health)*100)/ut[j]._health))
        for j in range(len(opponent_team)):
            if ot[j]._health > 0:
                total_score -= round((((ot[j]._health - opponent_team[j]._health)*100)/ot[j]._health))
            
        
        if u1._health > 0:
            total_score += round((((u1._health - human1._health)*100)/u1._health))
        
        
        if u2._health > 0:
            total_score += round((((u2._health - human2._health)*100)/u2._health))
        
        
        if o1._health > 0:
            total_score -= round((((o1._health - main_computer._health)*100)/o1._health))
        
        
        if o2._health > 0:
            total_score -= round((((o2._health - computer2._health)*100)/o2._health))
        
        
        move2_totals.append([total_score, real_targets])        
        
        
        
        
        
        
        
    possible_targets = []
    possible_target_results = []
    
    for k in range(len(move2_totals)):
        if move2_totals[k][1] not in possible_targets:
            possible_targets.append(move2_totals[k][1])
            
    for k in range(len(possible_targets)):
        sim_score = 0
        sim_target_count = 0
        for j in range(len(move2_totals)):
            if possible_targets[k] == move2_totals[j][1]:
                sim_target_count += 1
                sim_score += move2_totals[j][0]
        sim_score = round(sim_score/sim_target_count)
        possible_target_results.append([sim_score,possible_targets[k]])
    
    
    maximum = 'none'
    max_score = -99999
    
    for k in range(len(possible_target_results)):
        if possible_target_results[k][0] > max_score:
            max_score = possible_target_results[k][0]
            maximum = possible_target_results[k][1]
            
    move2_totals = [max_score,maximum]
    
# using third move -------------------------------------------------------------------------------------------------------------------------------------------------------       
    
    for i in range(total_sims):
        
        human1, human2, main_computer, computer2, user_team, opponent_team = copy.deepcopy(u1), copy.deepcopy(u2), copy.deepcopy(opponent), copy.deepcopy(o2), copy.deepcopy(ut), copy.deepcopy(ot)
        
        currentfield_sim._rain = currentfield._rain
        currentfield_sim._hailing = currentfield._hailing
        currentfield_sim._sand_storm = currentfield._sand_storm
        currentfield_sim._grass = currentfield._grass
        currentfield_sim._raincount = currentfield._raincount
        currentfield_sim._hailcount = currentfield._hailcount
        currentfield_sim._sand_stormcount = currentfield._sand_stormcount
        currentfield_sim._grasscount = currentfield._grasscount
        currentfield_sim._background = currentfield._background
        currentfield_sim._status = currentfield._status
        currentfield_sim._trickroom = currentfield._trickroom
        currentfield_sim._trickroomcount = currentfield._trickroomcount
        

        team_1_config_sim._wish1_active = team_1_config._wish1_active
        team_1_config_sim._wish2_active = team_1_config._wish2_active
        team_2_config_sim._wish1_active = team_2_config._wish1_active
        team_2_config_sim._wish2_active = team_2_config._wish2_active
        
        team_1_config_sim._aquaring = team_1_config._aquaring
        team_1_config_sim._aquaringcount = team_1_config._aquaringcount
        team_2_config_sim._aquaring = team_2_config._aquaring
        team_2_config_sim._aquaringcount = team_2_config._aquaringcount
        

        
        
        
        simulated_field._first_user = human1
        simulated_field._second_user = human2
        simulated_field._first_computer = main_computer
        simulated_field._second_computer = computer2
        
        
        
        team1clouds_sim[0] = team1clouds[0]
        team2clouds_sim[0] = team2clouds[0]
        
        
        human1._move_selected, human1._targets = 'none','none'
        human2._move_selected, human2._targets = 'none','none'
        main_computer._move_selected, main_computer._targets = 'none','none'
        computer2._move_selected, computer2._targets = 'none','none'
        
        for k in range(len(user_team)):
            user_team[k]._move_selected, user_team[k]._targets = 'none','none'
        for k in range(len(opponent_team)):
            opponent_team[k]._move_selected, opponent_team[k]._targets = 'none','none'
            
       
        main_computer._move_selected = main_computer._move3
        
        all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
        
        first_targets = all_targets[0]
        
        real_targets = all_targets[1]
        
        main_computer._targets = first_targets
        
        first_attack = True
        
        
        
        
        for battle_round in range(5):
            
            user_total_health = 0
            user_total_health += simulated_field._first_user._health
            user_total_health += simulated_field._second_user._health
            for g in range(len(user_team)):
                user_total_health += user_team[g]._health
                
            computer_total_health = 0
            computer_total_health += simulated_field._first_computer._health
            computer_total_health += simulated_field._second_computer._health
            for g in range(len(opponent_team)):
                computer_total_health += user_team[g]._health
            
            if computer_total_health == 0 or user_total_health == 0:
                break
            
            if first_attack:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
                    
            else:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._first_computer._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
            
            
            if simulated_field._first_user._last_move == 'rollout':
                simulated_field._first_user._last_move = 'none'
                 
            if simulated_field._second_user._last_move == 'rollout':
                simulated_field._second_user._last_move = 'none'
                    
            if simulated_field._first_computer._last_move == 'rollout':
                simulated_field._first_computer._last_move = 'none'
                
            if simulated_field._second_computer._last_move == 'rollout':
                simulated_field._second_computer._last_move = 'none'
                 
             
                        
            #assign moves
            
            if first_attack:
                
                if user_number == 2:
                    if first_opponent_simulation[0] == 'none':
        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                    elif first_opponent_simulation[0] == 'swap':
                        
                        x = copy.deepcopy(simulated_field._second_computer)
                        
                        for k in range(ot):
                            if ot[k] == new_opponent[0]:
                                y = copy.deepcopy(opponent_team[k])
                                index = k
                                
                        simulated_field._second_computer = y
                        opponent_team.remove(opponent_team[index])
                        opponent_team._append(x)
                        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                        
                        
                        
                    else:
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        computer2._move_selected = first_opponent_simulation[0][0]
                        computer2._targets = first_opponent_simulation[0][1]
                        
                        
                        first_attack = False
                        
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                    
                    
                else:  
                    if can_user_select_move_sim(human1):
                        human1._move_selected = choose_random_move_sim(human1)
                        human1._targets = return_targets(human1._move_selected, human1)
                        human1._can_move = True
                    else:
                        human1._can_move = False
                        
                    if can_user_select_move_sim(human2):
                        human2._move_selected = choose_random_move_sim(human2)
                        human2._targets = return_targets(human2._move_selected, human2)
                        human2._can_move = True
                    else:
                        human2._can_move = False
                        
                    if can_user_select_move_sim(computer2):
                        computer2._move_selected = choose_random_move_sim(computer2)
                        computer2._targets = return_targets(computer2._move_selected, computer2)
                        computer2._can_move = True
                    else:
                        computer2._can_move = False
                        
                    
                    first_attack = False
                
                    all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                
                
            else:
                        
                if can_user_select_move_sim(simulated_field._first_user):
                    simulated_field._first_user._move_selected = choose_random_move_sim(simulated_field._first_user)
                    simulated_field._first_user._targets = return_targets(simulated_field._first_user._move_selected, simulated_field._first_user)
                    simulated_field._first_user._can_move = True
                else:
                    simulated_field._first_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_user):
                    simulated_field._second_user._move_selected = choose_random_move_sim(simulated_field._second_user)
                    simulated_field._second_user._targets = return_targets(simulated_field._second_user._move_selected, simulated_field._second_user)
                    simulated_field._second_user._can_move = True
                else:
                    simulated_field._second_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_computer):
                    simulated_field._second_computer._move_selected = choose_random_move_sim(simulated_field._second_computer)
                    simulated_field._second_computer._targets = return_targets(simulated_field._second_computer._move_selected, simulated_field._second_computer)
                    simulated_field._second_computer._can_move = True
                else:
                    simulated_field._second_computer._can_move = False
                    
                if can_user_select_move_sim(simulated_field._first_computer):
                    simulated_field._first_computer._move_selected = choose_random_move_sim(simulated_field._first_computer)
                    simulated_field._first_computer._targets = return_targets(simulated_field._first_computer._move_selected, simulated_field._first_computer)
                    simulated_field._first_computer._can_move = True
                else:
                    simulated_field._first_computer._can_move = False
                
                
                
                all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
            
            
            #sorting by speed
            
            all_opponent_list.sort(key=lambda x: x._speed, reverse=True)
            
            
            if currentfield_sim._trickroom == True:
                all_opponent_list.sort(key=lambda x: x._speed, reverse=False)
            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
            
            
            for n in range(len(all_opponent_list)):
                try:
                    if all_opponent_list[n]._recharge == True:
                        all_opponent_list[n]._recharge = False
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'solar_beam_2'
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'meteor_beam_2'
                except:
                    pass
                
                
              
            if team_1_config_sim._wish1_active:
                if simulated_field._first_user._health > 0:
                    heal_sim(simulated_field._first_user._health, round(simulated_field._first_user._health/2))
                team_1_config_sim._wish1_active = False
                
            if team_1_config_sim._wish2_active:
                if simulated_field._second_user._health > 0:
                    heal_sim(simulated_field._second_user._health, round(simulated_field._second_user._health/2))
                team_1_config_sim._wish2_active = False
                
            if team_2_config_sim._wish1_active:
                if simulated_field._first_computer._health > 0:
                    heal_sim(simulated_field._first_computer._health, round(simulated_field._first_computer._health/2))
                team_2_config_sim._wish1_active = False
                
            if team_2_config_sim._wish2_active:
                if simulated_field._second_computer._health > 0:
                    heal_sim(simulated_field._second_computer._health, round(simulated_field._second_computer._health/2))
                team_2_config_sim._wish2_active = False
                
                
               
               
            
            for move_user in range(len(all_opponent_list)):
               if can_user_move_sim(all_opponent_list[move_user]):
                   
                   
                   if all_opponent_list[move_user]._condition == 'alive':
                        if all_opponent_list[move_user]._move_selected == 'instruct':
                            
                             if all_opponent_list[move_user] == simulated_field._first_user:
                                 ally = simulated_field._second_user
                             if all_opponent_list[move_user] == simulated_field._second_user:
                                 ally = simulated_field._first_user
                             if all_opponent_list[move_user] == simulated_field._first_computer:
                                 ally = simulated_field._second_computer
                             if all_opponent_list[move_user] == simulated_field._second_computer:
                                 ally = simulated_field._first_computer
                                
                             if ally._condition == 'alive' and ally._can_move and ally._recharge == False and ally._chargeup_solar == False and ally._chargeup_meteor == False and ally._last_move != 'instruct' and ally._last_move != 'mirror_move' and instruct_check(ally):
                                 eval(ally[move_user]._move_selected + '_sim')(ally[move_user], ally[move_user]._targets)
                                 
                        
                        elif all_opponent_list[move_user]._move_selected == 'quash':
                            all_opponent_list[move_user]._priority -= 10
                            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                        else:
                            eval(all_opponent_list[move_user]._move_selected + '_sim')(all_opponent_list[move_user], all_opponent_list[move_user]._targets)
                            all_opponent_list[move_user]._last_move = all_opponent_list[move_user]._move_selected
                            
                        checkhealth_sim()
                     
                   
            checkstatuses_sim()        
            checkhealth_round_end_sim(user_team,opponent_team)
        
        
        
        
        
        
        
        
        
        
        
        
        total_score = 0
        
        for j in range(len(user_team)):
            if ut[j]._health > 0:  
                total_score += round((((ut[j]._health - user_team[j]._health)*100)/ut[j]._health))
        for j in range(len(opponent_team)):
            if ot[j]._health > 0:
                total_score -= round((((ot[j]._health - opponent_team[j]._health)*100)/ot[j]._health))
            
        
        if u1._health > 0:
            total_score += round((((u1._health - human1._health)*100)/u1._health))
        
        
        if u2._health > 0:
            total_score += round((((u2._health - human2._health)*100)/u2._health))
        
        
        if o1._health > 0:
            total_score -= round((((o1._health - main_computer._health)*100)/o1._health))
        
        
        if o2._health > 0:
            total_score -= round((((o2._health - computer2._health)*100)/o2._health))
        
        
        move3_totals.append([total_score, real_targets])        
        
        
        
        
        
        
        
    possible_targets = []
    possible_target_results = []
    
    for k in range(len(move3_totals)):
        if move3_totals[k][1] not in possible_targets:
            possible_targets.append(move3_totals[k][1])
            
    for k in range(len(possible_targets)):
        sim_score = 0
        sim_target_count = 0
        for j in range(len(move3_totals)):
            if possible_targets[k] == move3_totals[j][1]:
                sim_target_count += 1
                sim_score += move3_totals[j][0]
        sim_score = round(sim_score/sim_target_count)
        possible_target_results.append([sim_score,possible_targets[k]])
    
    
    maximum = 'none'
    max_score = -99999
    
    for k in range(len(possible_target_results)):
        if possible_target_results[k][0] > max_score:
            max_score = possible_target_results[k][0]
            maximum = possible_target_results[k][1]
            
    move3_totals = [max_score,maximum]


# using fourth move -------------------------------------------------------------------------------------------------------------------------------------------------------       
    
    for i in range(total_sims):
        
        human1, human2, main_computer, computer2, user_team, opponent_team = copy.deepcopy(u1), copy.deepcopy(u2), copy.deepcopy(opponent), copy.deepcopy(o2), copy.deepcopy(ut), copy.deepcopy(ot)
        
        currentfield_sim._rain = currentfield._rain
        currentfield_sim._hailing = currentfield._hailing
        currentfield_sim._sand_storm = currentfield._sand_storm
        currentfield_sim._grass = currentfield._grass
        currentfield_sim._raincount = currentfield._raincount
        currentfield_sim._hailcount = currentfield._hailcount
        currentfield_sim._sand_stormcount = currentfield._sand_stormcount
        currentfield_sim._grasscount = currentfield._grasscount
        currentfield_sim._background = currentfield._background
        currentfield_sim._status = currentfield._status
        currentfield_sim._trickroom = currentfield._trickroom
        currentfield_sim._trickroomcount = currentfield._trickroomcount
        

        team_1_config_sim._wish1_active = team_1_config._wish1_active
        team_1_config_sim._wish2_active = team_1_config._wish2_active
        team_2_config_sim._wish1_active = team_2_config._wish1_active
        team_2_config_sim._wish2_active = team_2_config._wish2_active
        
        team_1_config_sim._aquaring = team_1_config._aquaring
        team_1_config_sim._aquaringcount = team_1_config._aquaringcount
        team_2_config_sim._aquaring = team_2_config._aquaring
        team_2_config_sim._aquaringcount = team_2_config._aquaringcount
        

        
        
        
        simulated_field._first_user = human1
        simulated_field._second_user = human2
        simulated_field._first_computer = main_computer
        simulated_field._second_computer = computer2
        
        
        
        team1clouds_sim[0] = team1clouds[0]
        team2clouds_sim[0] = team2clouds[0]
        
        
        human1._move_selected, human1._targets = 'none','none'
        human2._move_selected, human2._targets = 'none','none'
        main_computer._move_selected, main_computer._targets = 'none','none'
        computer2._move_selected, computer2._targets = 'none','none'
        
        for k in range(len(user_team)):
            user_team[k]._move_selected, user_team[k]._targets = 'none','none'
        for k in range(len(opponent_team)):
            opponent_team[k]._move_selected, opponent_team[k]._targets = 'none','none'
            
       
        main_computer._move_selected = main_computer._move4
        
        all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
        
        first_targets = all_targets[0]
        
        real_targets = all_targets[1]
        
        main_computer._targets = first_targets
        
        first_attack = True
        
        
        
        
        for battle_round in range(5):
            
            user_total_health = 0
            user_total_health += simulated_field._first_user._health
            user_total_health += simulated_field._second_user._health
            for g in range(len(user_team)):
                user_total_health += user_team[g]._health
                
            computer_total_health = 0
            computer_total_health += simulated_field._first_computer._health
            computer_total_health += simulated_field._second_computer._health
            for g in range(len(opponent_team)):
                computer_total_health += user_team[g]._health
            
            if computer_total_health == 0 or user_total_health == 0:
                break
            
            if first_attack:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
                    
            else:
                simulated_field._first_user._priority = 0
                simulated_field._second_user._priority = 0
                simulated_field._first_computer._priority = 0
                simulated_field._second_computer._priority = 0
                
                simulated_field._first_user._helped = False
                simulated_field._second_user._helped = False
                simulated_field._first_computer._helped = False
                simulated_field._second_computer._helped = False

                for n in range(len(user_team)):
                    user_team[n]._helped = False
                for n in range(len(opponent_team)):
                    cpu_pokelist[n]._helped = False
            
            
            if simulated_field._first_user._last_move == 'rollout':
                simulated_field._first_user._last_move = 'none'
                 
            if simulated_field._second_user._last_move == 'rollout':
                simulated_field._second_user._last_move = 'none'
                    
            if simulated_field._first_computer._last_move == 'rollout':
                simulated_field._first_computer._last_move = 'none'
                
            if simulated_field._second_computer._last_move == 'rollout':
                simulated_field._second_computer._last_move = 'none'
                 
             
                        
            #assign moves
            
            if first_attack:
                
                if user_number == 2:
                    if first_opponent_simulation[0] == 'none':
        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                    elif first_opponent_simulation[0] == 'swap':
                        
                        x = copy.deepcopy(simulated_field._second_computer)
                        
                        for k in range(ot):
                            if ot[k] == new_opponent[0]:
                                y = copy.deepcopy(opponent_team[k])
                                index = k
                                
                        simulated_field._second_computer = y
                        opponent_team.remove(opponent_team[index])
                        opponent_team._append(x)
                        
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        first_attack = False
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                        
                        
                        
                        
                        
                    else:
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        
                        computer2._move_selected = first_opponent_simulation[0][0]
                        computer2._targets = first_opponent_simulation[0][1]
                        
                        
                        first_attack = False
                        
                        
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                    
                    
                else:  
                    if can_user_select_move_sim(human1):
                        human1._move_selected = choose_random_move_sim(human1)
                        human1._targets = return_targets(human1._move_selected, human1)
                        human1._can_move = True
                    else:
                        human1._can_move = False
                        
                    if can_user_select_move_sim(human2):
                        human2._move_selected = choose_random_move_sim(human2)
                        human2._targets = return_targets(human2._move_selected, human2)
                        human2._can_move = True
                    else:
                        human2._can_move = False
                        
                    if can_user_select_move_sim(computer2):
                        computer2._move_selected = choose_random_move_sim(computer2)
                        computer2._targets = return_targets(computer2._move_selected, computer2)
                        computer2._can_move = True
                    else:
                        computer2._can_move = False
                        
                    
                    first_attack = False
                
                    all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                
                
            else:
                        
                if can_user_select_move_sim(simulated_field._first_user):
                    simulated_field._first_user._move_selected = choose_random_move_sim(simulated_field._first_user)
                    simulated_field._first_user._targets = return_targets(simulated_field._first_user._move_selected, simulated_field._first_user)
                    simulated_field._first_user._can_move = True
                else:
                    simulated_field._first_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_user):
                    simulated_field._second_user._move_selected = choose_random_move_sim(simulated_field._second_user)
                    simulated_field._second_user._targets = return_targets(simulated_field._second_user._move_selected, simulated_field._second_user)
                    simulated_field._second_user._can_move = True
                else:
                    simulated_field._second_user._can_move = False
                    
                if can_user_select_move_sim(simulated_field._second_computer):
                    simulated_field._second_computer._move_selected = choose_random_move_sim(simulated_field._second_computer)
                    simulated_field._second_computer._targets = return_targets(simulated_field._second_computer._move_selected, simulated_field._second_computer)
                    simulated_field._second_computer._can_move = True
                else:
                    simulated_field._second_computer._can_move = False
                    
                if can_user_select_move_sim(simulated_field._first_computer):
                    simulated_field._first_computer._move_selected = choose_random_move_sim(simulated_field._first_computer)
                    simulated_field._first_computer._targets = return_targets(simulated_field._first_computer._move_selected, simulated_field._first_computer)
                    simulated_field._first_computer._can_move = True
                else:
                    simulated_field._first_computer._can_move = False
                
                
                
                all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
            
            
            #sorting by speed
            
            all_opponent_list.sort(key=lambda x: x._speed, reverse=True)
            
            
            if currentfield_sim._trickroom == True:
                all_opponent_list.sort(key=lambda x: x._speed, reverse=False)
            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
            
            
            for n in range(len(all_opponent_list)):
                try:
                    if all_opponent_list[n]._recharge == True:
                        all_opponent_list[n]._recharge = False
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'solar_beam_2'
                except:
                    pass
                
                
                try:
                    if all_opponent_list[n]._chargeup_solar == True:
                        all_opponent_list[n]._chargeup_solar = False
                        all_opponent_list[n]._move_selected = 'meteor_beam_2'
                except:
                    pass
                
                
              
            if team_1_config_sim._wish1_active:
                if simulated_field._first_user._health > 0:
                    heal_sim(simulated_field._first_user._health, round(simulated_field._first_user._health/2))
                team_1_config_sim._wish1_active = False
                
            if team_1_config_sim._wish2_active:
                if simulated_field._second_user._health > 0:
                    heal_sim(simulated_field._second_user._health, round(simulated_field._second_user._health/2))
                team_1_config_sim._wish2_active = False
                
            if team_2_config_sim._wish1_active:
                if simulated_field._first_computer._health > 0:
                    heal_sim(simulated_field._first_computer._health, round(simulated_field._first_computer._health/2))
                team_2_config_sim._wish1_active = False
                
            if team_2_config_sim._wish2_active:
                if simulated_field._second_computer._health > 0:
                    heal_sim(simulated_field._second_computer._health, round(simulated_field._second_computer._health/2))
                team_2_config_sim._wish2_active = False
                
                
               
               
            
            for move_user in range(len(all_opponent_list)):
               if can_user_move_sim(all_opponent_list[move_user]):
                   
                   
                   if all_opponent_list[move_user]._condition == 'alive':
                        if all_opponent_list[move_user]._move_selected == 'instruct':
                            
                             if all_opponent_list[move_user] == simulated_field._first_user:
                                 ally = simulated_field._second_user
                             if all_opponent_list[move_user] == simulated_field._second_user:
                                 ally = simulated_field._first_user
                             if all_opponent_list[move_user] == simulated_field._first_computer:
                                 ally = simulated_field._second_computer
                             if all_opponent_list[move_user] == simulated_field._second_computer:
                                 ally = simulated_field._first_computer
                                
                             if ally._condition == 'alive' and ally._can_move and ally._recharge == False and ally._chargeup_solar == False and ally._chargeup_meteor == False and ally._last_move != 'instruct' and ally._last_move != 'mirror_move' and instruct_check(ally):
                                 eval(ally[move_user]._move_selected + '_sim')(ally[move_user], ally[move_user]._targets)
                                 
                        
                        elif all_opponent_list[move_user]._move_selected == 'quash':
                            all_opponent_list[move_user]._priority -= 10
                            all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                        else:
                            eval(all_opponent_list[move_user]._move_selected + '_sim')(all_opponent_list[move_user], all_opponent_list[move_user]._targets)
                            all_opponent_list[move_user]._last_move = all_opponent_list[move_user]._move_selected
                            
                        checkhealth_sim()
                     
                   
            checkstatuses_sim()        
            checkhealth_round_end_sim(user_team,opponent_team)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        total_score = 0
        
        for j in range(len(user_team)):
            if ut[j]._health > 0:  
                total_score += round((((ut[j]._health - user_team[j]._health)*100)/ut[j]._health))
        for j in range(len(opponent_team)):
            if ot[j]._health > 0:
                total_score -= round((((ot[j]._health - opponent_team[j]._health)*100)/ot[j]._health))
            
        
        if u1._health > 0:
            total_score += round((((u1._health - human1._health)*100)/u1._health))
        
        
        if u2._health > 0:
            total_score += round((((u2._health - human2._health)*100)/u2._health))
        
        
        if o1._health > 0:
            total_score -= round((((o1._health - main_computer._health)*100)/o1._health))
        
        
        if o2._health > 0:
            total_score -= round((((o2._health - computer2._health)*100)/o2._health))
        
        
        move4_totals.append([total_score, real_targets])        
        
        
        
        
        
        
        
    possible_targets = []
    possible_target_results = []
    
    for k in range(len(move4_totals)):
        if move4_totals[k][1] not in possible_targets:
            possible_targets.append(move4_totals[k][1])
            
    for k in range(len(possible_targets)):
        sim_score = 0
        sim_target_count = 0
        for j in range(len(move4_totals)):
            if possible_targets[k] == move4_totals[j][1]:
                sim_target_count += 1
                sim_score += move4_totals[j][0]
        sim_score = round(sim_score/sim_target_count)
        possible_target_results.append([sim_score,possible_targets[k]])
    
    
    maximum = 'none'
    max_score = -99999
    
    for k in range(len(possible_target_results)):
        if possible_target_results[k][0] > max_score:
            max_score = possible_target_results[k][0]
            maximum = possible_target_results[k][1]
            
    move4_totals = [max_score,maximum]


# swaps -----------------------------------------------------------------------------------------------------------------------------------------

    for i in range(total_sims):
        
        human1, human2, main_computer, computer2, user_team, opponent_team = copy.deepcopy(u1), copy.deepcopy(u2), copy.deepcopy(opponent), copy.deepcopy(o2), copy.deepcopy(ut), copy.deepcopy(ot)
        
        currentfield_sim._rain = currentfield._rain
        currentfield_sim._hailing = currentfield._hailing
        currentfield_sim._sand_storm = currentfield._sand_storm
        currentfield_sim._grass = currentfield._grass
        currentfield_sim._raincount = currentfield._raincount
        currentfield_sim._hailcount = currentfield._hailcount
        currentfield_sim._sand_stormcount = currentfield._sand_stormcount
        currentfield_sim._grasscount = currentfield._grasscount
        currentfield_sim._background = currentfield._background
        currentfield_sim._status = currentfield._status
        currentfield_sim._trickroom = currentfield._trickroom
        currentfield_sim._trickroomcount = currentfield._trickroomcount
        

        team_1_config_sim._wish1_active = team_1_config._wish1_active
        team_1_config_sim._wish2_active = team_1_config._wish2_active
        team_2_config_sim._wish1_active = team_2_config._wish1_active
        team_2_config_sim._wish2_active = team_2_config._wish2_active
        
        team_1_config_sim._aquaring = team_1_config._aquaring
        team_1_config_sim._aquaringcount = team_1_config._aquaringcount
        team_2_config_sim._aquaring = team_2_config._aquaring
        team_2_config_sim._aquaringcount = team_2_config._aquaringcount
        

        
        
        
        simulated_field._first_user = human1
        simulated_field._second_user = human2
        simulated_field._first_computer = main_computer
        simulated_field._second_computer = computer2
        
        
        
        team1clouds_sim[0] = team1clouds[0]
        team2clouds_sim[0] = team2clouds[0]
        
        
        human1._move_selected, human1._targets = 'none','none'
        human2._move_selected, human2._targets = 'none','none'
        main_computer._move_selected, main_computer._targets = 'none','none'
        computer2._move_selected, computer2._targets = 'none','none'
        
        for k in range(len(user_team)):
            user_team[k]._move_selected, user_team[k]._targets = 'none','none'
        for k in range(len(opponent_team)):
            opponent_team[k]._move_selected, opponent_team[k]._targets = 'none','none'
            
        if user_number == 2:    
            potential_alive = []
            potential_alive_real = []
            for n in range(opponent_team):
                if opponent_team[n]._status == 'alive' and opponent_team[n]._health > 0 and ot[n] != new_opponent[0]:
                    potential_alive.append(opponent_team[n])
                    potential_alive_real.append(ot[n])
            
            if len(potential_alive) > 0:
                target_random_chance = random.randrange(0,len(potential_alive))       
                if main_computer._snaptrap_def != False and 'elusive' not in main_computer._abilities or main_computer._infested_def != False and 'elusive' not in main_computer._abilities:
                    x = copy.deepcopy(simulated_field._first_computer)
                    y = copy.deepcopy(potential_alive[target_random_chance])
                    real_targets = [potential_alive_real[target_random_chance]]
                    simulated_field._first_computer = y
                    opponent_team.remove(potential_alive[target_random_chance])
                    opponent_team._append(x)
           
                main_computer._move_selected = 'swap'
                
                all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
                
                first_targets = all_targets[0]
                
                real_targets = all_targets[1]
                
                main_computer._targets = first_targets
                
                first_attack = True
                
            else:
                potential_alive = []
                potential_alive_real = []
                for n in range(opponent_team):
                    if opponent_team[n]._status == 'alive' and opponent_team[n]._health > 0:
                        potential_alive.append(opponent_team[n])
                        potential_alive_real.append(ot[n])
                
                if len(potential_alive) > 0:
                    target_random_chance = random.randrange(0,len(potential_alive))       
                    if main_computer._snaptrap_def != False and 'elusive' not in main_computer._abilities or main_computer._infested_def != False and 'elusive' not in main_computer._abilities:
                        x = copy.deepcopy(simulated_field._first_computer)
                        y = copy.deepcopy(potential_alive[target_random_chance])
                        real_targets = [potential_alive_real[target_random_chance]]
                        simulated_field._first_computer = y
                        opponent_team.remove(potential_alive[target_random_chance])
                        opponent_team._append(x)
               
                    main_computer._move_selected = 'swap'
                    
                    all_targets = return_targets_main(main_computer._move_selected, main_computer, u1, u2, o1, o2,opponent)
                    
                    first_targets = all_targets[0]
                    
                    real_targets = all_targets[1]
                    
                    main_computer._targets = first_targets
                    
                    first_attack = True
            
            
            
            
            for battle_round in range(5):
                
                user_total_health = 0
                user_total_health += simulated_field._first_user._health
                user_total_health += simulated_field._second_user._health
                for g in range(len(user_team)):
                    user_total_health += user_team[g]._health
                    
                computer_total_health = 0
                computer_total_health += simulated_field._first_computer._health
                computer_total_health += simulated_field._second_computer._health
                for g in range(len(opponent_team)):
                    computer_total_health += user_team[g]._health
                
                if computer_total_health == 0 or user_total_health == 0:
                    break
                
                if first_attack:
                    simulated_field._first_user._priority = 0
                    simulated_field._second_user._priority = 0
                    simulated_field._second_computer._priority = 0
                    
                    simulated_field._first_user._helped = False
                    simulated_field._second_user._helped = False
                    simulated_field._first_computer._helped = False
                    simulated_field._second_computer._helped = False

                    for n in range(len(user_team)):
                        user_team[n]._helped = False
                    for n in range(len(opponent_team)):
                        cpu_pokelist[n]._helped = False
                        
                else:
                    simulated_field._first_user._priority = 0
                    simulated_field._second_user._priority = 0
                    simulated_field._first_computer._priority = 0
                    simulated_field._second_computer._priority = 0
                    
                    simulated_field._first_user._helped = False
                    simulated_field._second_user._helped = False
                    simulated_field._first_computer._helped = False
                    simulated_field._second_computer._helped = False

                    for n in range(len(user_team)):
                        user_team[n]._helped = False
                    for n in range(len(opponent_team)):
                        cpu_pokelist[n]._helped = False
                
                
                if simulated_field._first_user._last_move == 'rollout':
                    simulated_field._first_user._last_move = 'none'
                     
                if simulated_field._second_user._last_move == 'rollout':
                    simulated_field._second_user._last_move = 'none'
                        
                if simulated_field._first_computer._last_move == 'rollout':
                    simulated_field._first_computer._last_move = 'none'
                    
                if simulated_field._second_computer._last_move == 'rollout':
                    simulated_field._second_computer._last_move = 'none'
                     
                 
                            
                #assign moves
                
                if first_attack:
                    
                    if user_number == 2:
                        if first_opponent_simulation[0] == 'none':
            
                            if can_user_select_move_sim(human1):
                                human1._move_selected = choose_random_move_sim(human1)
                                human1._targets = return_targets(human1._move_selected, human1)
                                human1._can_move = True
                            else:
                                human1._can_move = False
                                
                            if can_user_select_move_sim(human2):
                                human2._move_selected = choose_random_move_sim(human2)
                                human2._targets = return_targets(human2._move_selected, human2)
                                human2._can_move = True
                            else:
                                human2._can_move = False
                                
                            
                            first_attack = False
                            
                            all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                            
                            
                        elif first_opponent_simulation[0] == 'swap':
                            
                            x = copy.deepcopy(simulated_field._second_computer)
                            
                            for k in range(ot):
                                if ot[k] == new_opponent[0]:
                                    y = copy.deepcopy(opponent_team[k])
                                    index = k
                                    
                            simulated_field._second_computer = y
                            opponent_team.remove(opponent_team[index])
                            opponent_team._append(x)
                            
                            if can_user_select_move_sim(human1):
                                human1._move_selected = choose_random_move_sim(human1)
                                human1._targets = return_targets(human1._move_selected, human1)
                                human1._can_move = True
                            else:
                                human1._can_move = False
                                
                            if can_user_select_move_sim(human2):
                                human2._move_selected = choose_random_move_sim(human2)
                                human2._targets = return_targets(human2._move_selected, human2)
                                human2._can_move = True
                            else:
                                human2._can_move = False
                                
                            
                            first_attack = False
                            
                            all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer]
                            
                            
                            
                            
                            
                        else:
                            if can_user_select_move_sim(human1):
                                human1._move_selected = choose_random_move_sim(human1)
                                human1._targets = return_targets(human1._move_selected, human1)
                                human1._can_move = True
                            else:
                                human1._can_move = False
                                
                            if can_user_select_move_sim(human2):
                                human2._move_selected = choose_random_move_sim(human2)
                                human2._targets = return_targets(human2._move_selected, human2)
                                human2._can_move = True
                            else:
                                human2._can_move = False
                                
                            
                            computer2._move_selected = first_opponent_simulation[0][0]
                            computer2._targets = first_opponent_simulation[0][1]
                            
                            
                            first_attack = False
                            
                            
                            all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                        
                        
                    else:  
                        if can_user_select_move_sim(human1):
                            human1._move_selected = choose_random_move_sim(human1)
                            human1._targets = return_targets(human1._move_selected, human1)
                            human1._can_move = True
                        else:
                            human1._can_move = False
                            
                        if can_user_select_move_sim(human2):
                            human2._move_selected = choose_random_move_sim(human2)
                            human2._targets = return_targets(human2._move_selected, human2)
                            human2._can_move = True
                        else:
                            human2._can_move = False
                            
                        if can_user_select_move_sim(computer2):
                            computer2._move_selected = choose_random_move_sim(computer2)
                            computer2._targets = return_targets(computer2._move_selected, computer2)
                            computer2._can_move = True
                        else:
                            computer2._can_move = False
                            
                        
                        first_attack = False
                    
                        all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                    
                    
                else:
                            
                    if can_user_select_move_sim(simulated_field._first_user):
                        simulated_field._first_user._move_selected = choose_random_move_sim(simulated_field._first_user)
                        simulated_field._first_user._targets = return_targets(simulated_field._first_user._move_selected, simulated_field._first_user)
                        simulated_field._first_user._can_move = True
                    else:
                        simulated_field._first_user._can_move = False
                        
                    if can_user_select_move_sim(simulated_field._second_user):
                        simulated_field._second_user._move_selected = choose_random_move_sim(simulated_field._second_user)
                        simulated_field._second_user._targets = return_targets(simulated_field._second_user._move_selected, simulated_field._second_user)
                        simulated_field._second_user._can_move = True
                    else:
                        simulated_field._second_user._can_move = False
                        
                    if can_user_select_move_sim(simulated_field._second_computer):
                        simulated_field._second_computer._move_selected = choose_random_move_sim(simulated_field._second_computer)
                        simulated_field._second_computer._targets = return_targets(simulated_field._second_computer._move_selected, simulated_field._second_computer)
                        simulated_field._second_computer._can_move = True
                    else:
                        simulated_field._second_computer._can_move = False
                        
                    if can_user_select_move_sim(simulated_field._first_computer):
                        simulated_field._first_computer._move_selected = choose_random_move_sim(simulated_field._first_computer)
                        simulated_field._first_computer._targets = return_targets(simulated_field._first_computer._move_selected, simulated_field._first_computer)
                        simulated_field._first_computer._can_move = True
                    else:
                        simulated_field._first_computer._can_move = False
                    
                    
                    
                    all_opponent_list = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
                
                
                #sorting by speed
                
                all_opponent_list.sort(key=lambda x: x._speed, reverse=True)
                
                
                if currentfield_sim._trickroom == True:
                    all_opponent_list.sort(key=lambda x: x._speed, reverse=False)
                all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                
                
                for n in range(len(all_opponent_list)):
                    try:
                        if all_opponent_list[n]._recharge == True:
                            all_opponent_list[n]._recharge = False
                    except:
                        pass
                    
                    
                    try:
                        if all_opponent_list[n]._chargeup_solar == True:
                            all_opponent_list[n]._chargeup_solar = False
                            all_opponent_list[n]._move_selected = 'solar_beam_2'
                    except:
                        pass
                    
                    
                    try:
                        if all_opponent_list[n]._chargeup_solar == True:
                            all_opponent_list[n]._chargeup_solar = False
                            all_opponent_list[n]._move_selected = 'meteor_beam_2'
                    except:
                        pass
                    
                    
                  
                if team_1_config_sim._wish1_active:
                    if simulated_field._first_user._health > 0:
                        heal_sim(simulated_field._first_user._health, round(simulated_field._first_user._health/2))
                    team_1_config_sim._wish1_active = False
                    
                if team_1_config_sim._wish2_active:
                    if simulated_field._second_user._health > 0:
                        heal_sim(simulated_field._second_user._health, round(simulated_field._second_user._health/2))
                    team_1_config_sim._wish2_active = False
                    
                if team_2_config_sim._wish1_active:
                    if simulated_field._first_computer._health > 0:
                        heal_sim(simulated_field._first_computer._health, round(simulated_field._first_computer._health/2))
                    team_2_config_sim._wish1_active = False
                    
                if team_2_config_sim._wish2_active:
                    if simulated_field._second_computer._health > 0:
                        heal_sim(simulated_field._second_computer._health, round(simulated_field._second_computer._health/2))
                    team_2_config_sim._wish2_active = False
                    
                    
                   
                   
                
                for move_user in range(len(all_opponent_list)):
                   if can_user_move_sim(all_opponent_list[move_user]):
                       
                       
                       if all_opponent_list[move_user]._condition == 'alive':
                            if all_opponent_list[move_user]._move_selected == 'instruct':
                                
                                 if all_opponent_list[move_user] == simulated_field._first_user:
                                     ally = simulated_field._second_user
                                 if all_opponent_list[move_user] == simulated_field._second_user:
                                     ally = simulated_field._first_user
                                 if all_opponent_list[move_user] == simulated_field._first_computer:
                                     ally = simulated_field._second_computer
                                 if all_opponent_list[move_user] == simulated_field._second_computer:
                                     ally = simulated_field._first_computer
                                    
                                 if ally._condition == 'alive' and ally._can_move and ally._recharge == False and ally._chargeup_solar == False and ally._chargeup_meteor == False and ally._last_move != 'instruct' and ally._last_move != 'mirror_move' and instruct_check(ally):
                                     eval(ally[move_user]._move_selected + '_sim')(ally[move_user], ally[move_user]._targets)
                                     
                            
                            elif all_opponent_list[move_user]._move_selected == 'quash':
                                all_opponent_list[move_user]._priority -= 10
                                all_opponent_list.sort(key=lambda x: x._priority, reverse=True)
                            else:
                                eval(all_opponent_list[move_user]._move_selected + '_sim')(all_opponent_list[move_user], all_opponent_list[move_user]._targets)
                                all_opponent_list[move_user]._last_move = all_opponent_list[move_user]._move_selected
                                
                            checkhealth_sim()
                         
                       
                checkstatuses_sim()        
                checkhealth_round_end_sim(user_team,opponent_team)
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            total_score = 0
            
            for j in range(len(user_team)):
                if ut[j]._health > 0:  
                    total_score += round((((ut[j]._health - user_team[j]._health)*100)/ut[j]._health))
            for j in range(len(opponent_team)):
                if ot[j]._health > 0:
                    total_score -= round((((ot[j]._health - opponent_team[j]._health)*100)/ot[j]._health))
                
            
            if u1._health > 0:
                total_score += round((((u1._health - human1._health)*100)/u1._health))
            
            
            if u2._health > 0:
                total_score += round((((u2._health - human2._health)*100)/u2._health))
            
            
            if o1._health > 0:
                total_score -= round((((o1._health - main_computer._health)*100)/o1._health))
            
            
            if o2._health > 0:
                total_score -= round((((o2._health - computer2._health)*100)/o2._health))
            
            
            move5_totals.append([total_score, real_targets])        
            
            
            
        
        
        
    if len(move5_totals):
        pass
    else:
        possible_targets = []
        possible_target_results = []
        
        for k in range(len(move5_totals)):
            if move5_totals[k][1] not in possible_targets:
                possible_targets.append(move5_totals[k][1])
                
        for k in range(len(possible_targets)):
            sim_score = 0
            sim_target_count = 0
            for j in range(len(move5_totals)):
                if possible_targets[k] == move5_totals[j][1]:
                    sim_target_count += 1
                    sim_score += move5_totals[j][0]
            sim_score = round(sim_score/sim_target_count)
            possible_target_results.append([sim_score,possible_targets[k]])
        
        
        maximum = 'none'
        max_score = -99999
        
        for k in range(len(possible_target_results)):
            if possible_target_results[k][0] > max_score:
                max_score = possible_target_results[k][0]
                maximum = possible_target_results[k][1]
                
        move5_totals = [max_score,maximum]
        
        
    
    move1_totals.append(opponent._move1)
    move2_totals.append(opponent._move2)
    move3_totals.append(opponent._move3)
    move4_totals.append(opponent._move4)

    
    final_results = [move1_totals,move2_totals,move3_totals,move4_totals]
    
    for i in range(len(final_results)):
        print(final_results[i][2])
        print(final_results[i][0])
        print()
    
    
    
    maximum = 'none'
    max_score = -99999
    
    for k in range(len(final_results)):
        if final_results[k][0] > max_score:
            max_score = final_results[k][0]
            final_score = final_results[k][0]
            attack_used = final_results[k][2]
            targets_used = final_results[k][1]
            
    
    if user_number == 1:
        if len(move5_totals) > 0:
            if move5_totals[0] > final_score:
                new_opponent[0] = move5_totals[1][0]  
                player2action[0] = 'newopponentpokemon(player1current, player2current, player1current2, player2current2, player1_pokelist, cpu_pokelist, trainer, background)'
                opponentaction[0] = 'swap'
                first_opponent_simulation[0] = 'swap'
            else:
                player2actiontarget[0] = targets_used
                player2action[0] = attack_used
                first_opponent_simulation[0] = [attack_used,targets_used]
                opponent._priority = move_priority_dict[attack_used]
        else:
            player2actiontarget[0] = targets_used
            player2action[0] = attack_used
            first_opponent_simulation[0] = [attack_used,targets_used]
            opponent._priority = move_priority_dict[attack_used]
    else:
        if len(move5_totals) > 0:
            if move5_totals[0] > final_score:
                new_opponent2[0] = move5_totals[1][0]  
                player2action2[0] = 'newopponentpokemon2(player1current, player2current, player1current2, player2current2, player1_pokelist, cpu_pokelist, trainer, background)'
                opponentaction2[0] = 'swap'
                second_opponent_simulation[0] = 'swap'
            else:
                player2actiontarget2[0] = targets_used
                player2action2[0] = attack_used
                second_opponent_simulation[0] = [attack_used,targets_used]
                opponent._priority = move_priority_dict[attack_used]
        else:
            player2actiontarget2[0] = targets_used
            player2action2[0] = attack_used
            second_opponent_simulation[0] = [attack_used,targets_used]
            opponent._priority = move_priority_dict[attack_used]
            
            





# SIMULATED STATUSES -------------------------------------------------------------------------------------------------------------------


def poison_sim(pokemon):
    if pokemon._status == 'normal':
        pokemon._status = 'poisoned'
        pokemon._poisoncount = 1
    
def freeze_sim(pokemon):
    if pokemon._status == 'normal':
        pokemon._status = 'frozen'
    
def burn_sim(pokemon):
    if pokemon._status == 'normal':
        pokemon._status = 'burned'
        pokemon._burncount = 1
    
def curse_sim(pokemon):
    if pokemon._cursed == False:
        pokemon._cursed = True
    
def paralyze_sim(pokemon):
    if pokemon._status == 'normal':
        pokemon._status = 'paralyzed'
    
    
def rain_sim():
    if currentfield_sim._status == 'normal':
        currentfield_sim._status = 'raining'
        currentfield_sim._rain = True
        currentfield_sim._raincount = 5
    elif currentfield_sim._status == 'raining':
        currentfield_sim._status = 'downpour'
        currentfield_sim._rain = True
        currentfield_sim._raincount = 5
    
    
def hail_sim():
    if currentfield_sim._status == 'normal':
        currentfield_sim._status = 'hailing'
        currentfield_sim._hailing = True
        currentfield_sim._hailcount = 5
    elif currentfield_sim._status == 'hailing':
        currentfield_sim._status = 'blizzard'
        currentfield_sim._hailing = True
        currentfield_sim._hailcount = 5
    


    
def sandstorm_sim():
    if currentfield_sim._status == 'normal':
        currentfield_sim._status = 'sandstorm'
        currentfield_sim._sand_storm = True
        currentfield_sim._sand_stormcount = 5
        

def grassy_terrain_sim():
    if currentfield_sim._status == 'normal':
        currentfield_sim._status = 'grassy_terrain'
        currentfield_sim._grass = True
        currentfield_sim._grasscount = 5
    

def sleep_sim(pokemon):
    if pokemon._status == 'normal':
        pokemon._status = 'sleeping'
        pokemon._sleepcount = 3
        if 'restless' in pokemon._abilities:
            pokemon._sleepcount = 2
            
    
    
def clear_statuses_sim(pokemon):    
    if pokemon._status == 'poisoned':
        pokemon._status = 'normal'
        pokemon._poisoncount = 0
    if pokemon._status == 'paralyzed':
        pokemon._status = 'normal'
    if pokemon._status == 'burned':
        pokemon._status = 'normal'
        pokemon._burncount = 0
    if pokemon._status == 'frozen':
        pokemon._status = 'normal'
        pokemon._burncount = 0
    if pokemon._status == 'sleeping':
        pokemon._status = 'normal'
        pokemon._sleepcount = 0
    
    
    
    
    
# STAT BUFS ----------------------------------------------------------------------------------------------------------------------------



def nerf_def_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._defense/pokemon._oridef > 0.25:
            pokemon._defense -= (pokemon._oridef * 0.05)
            
def nerf_atk_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._damage/pokemon._oriatk > 0.25:
            pokemon._damage -= (pokemon._oriatk * 0.05)
            
def nerf_spd_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._speed/pokemon._orispd > 0.25:
            pokemon._speed -= (pokemon._orispd * 0.05)
            
def nerf_acc_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._accuracy/pokemon._oriacc > 0.25:
            pokemon._accuracy -= (pokemon._oriacc * 0.05)
            
            
def buf_def_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._defense/pokemon._oridef < 4:
            pokemon._defense += (pokemon._oridef * 0.05)
            
def buf_atk_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._damage/pokemon._oriatk < 4:
            pokemon._damage += (pokemon._oriatk * 0.05)
            
def buf_spd_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._speed/pokemon._orispd < 4:
            pokemon._speed += (pokemon._orispd * 0.05)
            
def buf_acc_sim(pokemon,amount):
    for i in range(amount):
        if pokemon._accuracy/pokemon._oriacc < 4:
            pokemon._accuracy += (pokemon._oriacc * 0.05)
            
            
# HEALTH AND STATUS CHECKS  ----------------------------------------------------------------------------------------------------------------------------            




def checkhealth_sim():
    pokemon = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
    for i in range(4):
        if pokemon[i]._health <= 0:
            pokemon[i]._health = 0
            pokemon[i]._condition = 'fainted'
            
            
def checkhealth_round_end_sim(team1,team2):
    pokemon = [simulated_field._first_user, simulated_field._second_user, simulated_field._first_computer, simulated_field._second_computer]
    for i in range(4):
        if pokemon[i]._health <= 0:
            pokemon[i]._health = 0
            pokemon[i]._condition = 'fainted'
            if pokemon[i] == simulated_field._first_computer:
                for k in range(len(team2)):
                    if team2[k]._health > 0:
                        x = copy.deepcopy(simulated_field._first_computer)
                        y = copy.deepcopy(team2[k])
                        simulated_field._first_computer = y
                        team2.remove(team2[k])
                        team2.append(x)
                        break
                
            elif pokemon[i] == simulated_field._second_computer:
                for k in range(len(team2)):
                    if team2[k]._health > 0:
                        x = copy.deepcopy(simulated_field._second_computer)
                        y = copy.deepcopy(team2[k])
                        simulated_field._second_computer = y
                        team2.remove(team2[k])
                        team2.append(x)
                        break
                    
            if pokemon[i] == simulated_field._first_user:
                for k in range(len(team1)):
                    if team1[k]._health > 0:
                        x = copy.deepcopy(simulated_field._first_user)
                        y = copy.deepcopy(team1[k])
                        simulated_field._first_user = y
                        team1.remove(team1[k])
                        team1.append(x)
                        break
                    
            if pokemon[i] == simulated_field._second_user:
                for k in range(len(team1)):
                    if team1[k]._health > 0:
                        x = copy.deepcopy(simulated_field._second_user)
                        y = copy.deepcopy(team1[k])
                        simulated_field._second_user = y
                        team1.remove(team1[k])
                        team1.append(x)
                        break
            
            
            
# MOVE CALCULATIONS -------------------------------------------------------------------------------------------------------------------           
            
            
            
            
def calculate_sim_damage(damage, user, target, effective, not_effective, null_list, crit, movetype, hit_protect):
    multiplyer = 1
    for i in range(len(effective)):
        if target._element == effective[i]:
            multiplyer *= 2
        if target._element2 == effective[i]:
            multiplyer *= 2
    for i in range(len(not_effective)):
        if target._element == not_effective[i]:
            multiplyer *= 0.5
        if target._element2 == not_effective[i]:
            multiplyer *= 0.5
    for i in range(len(null_list)):
        if target._element == null_list[i]:
            multiplyer *= 0
        if target._element2 == null_list[i]:
            multiplyer *= 0
    
    if crit > random.randrange(0,100):
        damage *= 1.5
        
    if user._element == movetype or user._element2 == movetype:
        multiplyer *= 1.25
        
    if target._protected == True and hit_protect == False:
        multiplyer *= 0
    
    try:
        if user._helped == True:
            damage = round(damage * 1.5)
    except:
        pass
    
    if 'berserk' in user._abilities and user._health/user._orighealth <= 0.50:
        damage = round(damage * 1.50)
        
    if 'neuroforce' in user._abilities and multiplyer > 1:
        damage = round(damage * 1.50)
    
    if 'rain_warrior' in user._abilities and currentfield._rain == True:
        damage = round(damage * 1.50)
        
    if 'stone_dancer' in user._abilities and currentfield._sand_storm == True:
        damage = round(damage * 1.50)
        
    if currentfield_sim._status == 'raining' and movetype == 'fire':
        damage = round(damage * 0.50)
        
    if currentfield._status == 'downpour' and movetype == 'fire':
        damage = round(damage * 0)
        
    if currentfield._status == 'raining' and movetype == 'water':
        damage = round(damage * 1.25)
        
    if currentfield._status == 'downpour' and movetype == 'water':
        damage = round(damage * 1.50)
        
    if currentfield._status == 'grassy_terrain' and movetype == 'grass':
        damage = round(damage * 1.50)
        
    if currentfield._status == 'hailing' and movetype == 'grass':
        damage = round(damage * 0.50)
        
    if currentfield._status == 'blizzard' and movetype == 'grass':
        damage = round(damage * 0)
    
    damage = round((damage * (user._damage / target._defense)) * ((user._lvl + 12)/30))
    
    return round(multiplyer * damage * (user._damage/target._defense))
            


def heal_sim(user, health):
    if user._health == user._orighealth:
        return
    if user == simulated_field._first_user:
        ally = simulated_field._second_user
    if user == simulated_field._second_user:
        ally = simulated_field._first_user
    if user == simulated_field._first_computer:
        ally = simulated_field._second_computer
    if user == simulated_field._second_computer:
        ally = simulated_field._first_computer
    if ('shaman' in ally._abilities and ally._condition == 'alive') or ('shaman' in user._abilities and user._condition == 'alive'):
        health = round(health * 1.25)
        
    if (user._health + health) > user._orighealth:
        health = user._orighealth - user._health
    
    if user._health > user._orighealth:
        user._health = user._orighealth
        
    user._health += health
     
        
     
def calculate_acc_sim(user, accuracy, target, no_miss):
    accuracy_chance = random.randrange(0,101)
    if no_miss:
        return True
    elif user._accuracy >= target._speed:
        if accuracy_chance > (100-accuracy - ((10 * ((round(user._accuracy/target._speed) -1))))):
            return True
        else:
            return False
    else:
        if accuracy_chance > (100-accuracy - ((10 * ((round(target._speed/user._accuracy) -1))))):
            return True
        else:
            return False

        
     
            
            
# MOVES  ----------------------------------------------------------------------------------------------------------------------------                        
            


def swap_sim(user,target,team):
    if user._snaptrap_def != False and 'elusive' not in user._abilities or user._infested_def != False and 'elusive' not in user._abilities:
        if user == simulated_field._first_computer:
            x = copy.deepcopy(simulated_field._first_computer)
            y = copy.deepcopy(target)
            simulated_field._first_computer = y
            team.remove(target)
            team._append(x)
            
        elif user == simulated_field._second_computer:
            x = copy.deepcopy(simulated_field._second_computer)
            y = copy.deepcopy(target)
            simulated_field._second_computer = y
            team.remove(target)
            team._append(x)
        

    
    
    
    
    
    
    
    
    

            
