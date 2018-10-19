# EveVerboseKillmail - A python package for easy killmail processing




### Installation:

Install with pip:

````
pip3 install eve-verbose-killmail
````

Or for installing from source, clone the repository and then run:

````
python3 setup.py sdist
pip3 install dist/package_name.tar.gz
````

### How to use
If you give the Killmail constructor a unprocessed killmail from zKill's RedisQ: 

````
unprocessed_killmail = {
                "package":
                    {
                        "killID": 71443648,
                        "killmail":
                            {
                                "attackers":
                                    [{
                                        "alliance_id": 1354830081,
                                        "character_id": 992181402,
                                        "corporation_id": 1324429368,
                                        "damage_done": 4110,
                                        "final_blow": True,
                                        "security_status": -7.8,
                                        "ship_type_id": 605,
                                        "weapon_type_id": 2456
                                    }],
                                "killmail_id": 71443648,
                                "killmail_time": "2018-07-24T17:56:14Z",
                                "solar_system_id": 30003681,
                                "victim":
                                    {
                                        "alliance_id": 99007362,
                                        "character_id": 2114300996,
                                        "corporation_id": 98531953,
                                        "damage_taken": 4110,
                                        "position":
                                            {
                                                "x": -456877791246.22,
                                                "y": -83876045685.746,
                                                "z": 458094309170.23
                                            },
                                        "ship_type_id": 32878
                                    }
                            },
                        "zkb":
                            {
                                "locationID": 50006982,
                                "hash": "9ab505bacad3122d8648e2c4aa9a3c80ad67eedc",
                                "fittedValue": 2543013.41,
                                "totalValue": 7521431.46,
                                "points": 1,
                                "npc": False,
                                "solo": True,
                                "awox": False,
                                "href": "https://esi.evetech.net/v1/killmails/71443648/9ab505bacad3122d8648e2c4aa9a3c80ad67eedc/"
                            }
                    }
            }
````

the killmail object will then have the following attributes:
````
        id
        time

        value_total
        value_fitted
        value_ship

        final_blow_damage
        final_blow_damage_percent
        final_blow_ship_id
        final_blow_ship_name
        final_blow_ship_group_id
        final_blow_ship_group_name

        solar_system_id
        solar_system_name
        solar_system_security
        solar_system_class
        region_id
        region_name
        constellation_id
        constellation_name

        victim_damage_taken
        victim_char_name
        victim_corp_name
        victim_alliance_name
        victim_ship_id
        victim_ship_name
        victim_ship_group_id
        victim_ship_group_name

        attacker_is_solo
        attacker_is_npc
        attacker_is_awox
        attacker_amount
        attacker_char_names
        attacker_corp_names
        attacker_alliance_names
        attacker_ship_ids
        attacker_ship_names
        attacker_ship_group_ids
        attacker_ship_group_names
````

example:
````
>>from eve_verbose_killmail import Kilmail

>>killmail = Killmail(unprocessed_killmail)

>>print(killmail.solar_system_name)

DO6H-Q
````