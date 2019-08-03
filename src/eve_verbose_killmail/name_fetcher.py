import threading
import logging
import os
import csv
from eve_verbose_killmail.esi_call import EsiCall


class NameFetcher(threading.Thread):

    def __init__(self, unprocessed_killmail):
        threading.Thread.__init__(self)
        self.unprocessed_killmail = unprocessed_killmail
        self.logger = logging.getLogger(__name__)

    def extract_from_killmail(self):
        pass

    def return_results(self):
        pass

    @staticmethod
    def make_esi_call(ids):

        return EsiCall().makeCall(ids)

    '''Get the ship category (Destroyer, Frigate, HAC, etc.) from invGroupExtracted.csv or invGroup.csv'''
    def csv_inv_groups_scraper(self, group_id_list):
        group_name_list = []
        searched_ids = []

        self.logger.debug("trying to read invGroups.csv")

        '''Check if the smaller invGroupExtracted.csv has the right category already'''
        filepath_extracted = os.path.dirname(__file__) + "/ressources/invGroupsExtracted.csv"
        with open(filepath_extracted, newline='', encoding='utf-8') as p_r:
            inv_types_extracted = csv.reader(p_r)
            for row in inv_types_extracted:
                for l in range(0, len(group_id_list)):
                    if row[0] == str(group_id_list[l]):
                        searched_ids.append(group_id_list[l])
                        if row[1] not in group_name_list:
                            group_name_list.append(row[1])

        for i in range(0, len(searched_ids)):
            while searched_ids[i] in group_id_list:
                group_id_list.remove(searched_ids[i])

        self.logger.debug("trying to read invGroups.csv")

        '''Check the much bigger invGroup.csv for the rest and write the entry also to invGroupExtracted.csv'''
        if len(group_id_list) != 0:
            filepath = os.path.dirname(__file__) + "/ressources/invGroups.csv"
            with open(filepath, newline='', encoding='utf-8') as f:
                inv_types = csv.reader(f)
                for row in inv_types:
                    for l in range(0, len(group_id_list)):
                        if row[0] == str(group_id_list[l]):
                            if row[2] not in group_name_list:
                                group_name_list.append(row[2])
                                with open(filepath_extracted, 'a', newline='') as p_w:
                                    inv_types_extracted = csv.writer(p_w)
                                    inv_types_extracted.writerow([group_id_list[l], row[2]])

        self.logger.debug("Group Name List: {}".format(group_name_list))

        if group_name_list is []:
            group_name_list.append("")

        self.logger.debug("Group Name List: {}".format(group_name_list))

        return {"group_name_list": group_name_list}

    def csv_inv_types_scraper(self, ship_id_list):
        name_list = []
        group_id_list = []
        searched_ids = []

        filepath_extracted = os.path.dirname(__file__) + "/ressources/invTypesExtracted.csv"
        with open(filepath_extracted, newline='') as p_r:
            inv_types_extracted = csv.reader(p_r)
            for row in inv_types_extracted:
                for l in range(0, len(ship_id_list)):
                    if row[0] == str(ship_id_list[l]):
                        searched_ids.append(ship_id_list[l])
                        if row[2] not in name_list:
                            name_list.append(row[2])
                        if row[1] not in group_id_list:
                            group_id_list.append(row[1])

        for i in range(0, len(searched_ids)):
            while searched_ids[i] in ship_id_list:
                ship_id_list.remove(searched_ids[i])

        self.logger.debug("trying to read invTypes.csv")

        if len(ship_id_list) != 0:
            filepath = os.path.dirname(__file__) + "/ressources/invTypes.csv"
            with open(filepath, newline='', encoding='utf-8') as f:
                inv_types = csv.reader(f)
                for row in inv_types:
                    for l in range(0, len(ship_id_list)):
                        if row[0] == str(ship_id_list[l]):
                            if row[2] not in name_list:
                                name_list.append(row[2])
                                with open(filepath_extracted, 'a', newline='') as p_w:
                                    inv_types_extracted = csv.writer(p_w)
                                    inv_types_extracted.writerow([row[0], row[1], row[2]])
                            if row[1] not in group_id_list:
                                group_id_list.append(row[1])

        self.logger.debug("Name List: {}".format(name_list))
        self.logger.debug("Group ID List: {}".format(group_id_list))

        if name_list is []:
            name_list.append("")
        if group_id_list is []:
            group_id_list.append("")

        self.logger.debug("Name List: {}".format(name_list))
        self.logger.debug("Group ID List: {}".format(group_id_list))

        return {"name_list": name_list, "group_id_list": group_id_list}

    def csv_map_solar_systems_scraper(self, solar_system_id_list):
        solar_system_name_list = []
        solar_system_security_list = []
        region_id_list = []
        constellation_id_list = []

        self.logger.debug("trying to read mapSolarSystems.csv")

        filepath = os.path.dirname(__file__) + "/ressources/mapSolarSystems.csv"
        with open(filepath, newline='', encoding='utf-8') as f:
            inv_types = csv.reader(f)
            for row in inv_types:
                for l in range(0, len(solar_system_id_list)):
                    if row[2] == str(solar_system_id_list[l]):
                        solar_system_name_list.append(row[3])
                        region_id_list.append(row[0])
                        constellation_id_list.append(row[1])
                        solar_system_security_list.append(row[21])

        self.logger.debug("Solar System Name List: {}".format(solar_system_name_list))
        self.logger.debug("Solar System Security List: {}".format(solar_system_security_list))
        self.logger.debug("Region ID List: {}".format(region_id_list))
        self.logger.debug("Cosntellation ID List: {}".format(constellation_id_list))

        if solar_system_name_list is []:
            solar_system_name_list.append("")
        if solar_system_security_list is []:
            solar_system_security_list.append("")
        if region_id_list is []:
            region_id_list.append("")
        if constellation_id_list is []:
            constellation_id_list.append("")

        self.logger.debug("Solar System Name List: {}".format(solar_system_name_list))
        self.logger.debug("Solar System Security List: {}".format(solar_system_security_list))
        self.logger.debug("Region ID List: {}".format(region_id_list))
        self.logger.debug("Cosntellation ID List: {}".format(constellation_id_list))

        return {"solar_system_name_list": solar_system_name_list,
                "solar_system_security_list": solar_system_security_list,
                "region_id_list": region_id_list,
                "constellation_id_list": constellation_id_list}
