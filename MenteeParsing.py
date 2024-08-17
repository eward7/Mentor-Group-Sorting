from codecs import getencoder
import csv
from pickle import TRUE
import random
from dataclasses import dataclass
import pandas as pd
import os
import csv
import glob
from xlsxwriter import Workbook

@dataclass
class Mentor:
    '''Class to represent and store Mentors and their groups'''
    name: str
    country: str
    numof_M: int
    numof_F: int
    numof_Other: int
    group_size: int
    mentees: list
    asia_east: int
    europe_western: int
    north_america: int
    asia_central_south: int
    central_south_america: int
    middle_east_north_africa: int
    africa: int
    europe_eastern: int
    oceania: int
    asia_central_south_middle_east: int
    other_cont: int
    iteration: int



@dataclass
class Mentee:
    '''Class to represent Mentees and their information'''
    last_name: str
    first_name: str
    preferred_name: str
    pronouns: str
    gender: str
    brown_email: str
    alt_email: str
    citizenships: str
    country_single: str
    residence: str
    student_type: str
    summer_contact: str
    region: str





# Initializing the Mentors and Mentees Lists
''' Mentors List'''
MENTORS = list()

'''All Mentees List'''
MENTEES = list()


def parse_mentors(filename: str):
    """
    Method parses CSV file of Mentors with 2 columns: Full Name & Region

    :parameter filename is the string file name or path
    """
    mentors_df = pd.read_csv(filename)
    for row in mentors_df.itertuples():
        MENTORS.append(Mentor(row.FullName, row.Country, 0, 0, 0, 0, list(),0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


def parse_mentees(filename: str):
    """
    Method parses CSV file of Mentees with the below columns

    :parameter filename is the string file name or path
    """
    mentees_df = pd.read_csv(filename)
    for row in mentees_df.itertuples():
        MENTEES.append(Mentee(row.LastName, row.FirstName, row.PreferredName,
                              row.Pronouns, row.Gender, row.BrownEmail, row.AlternativeEmail,
                              row.Citizenships, row.CountrySingle, row.Residence, row.StudentType, row.SummerContact, row.Region))


def total_students_assigned():
    total = 0
    for mentor in MENTORS:
        print(mentor.name, mentor.group_size)
        print("male", mentor.numof_M)
        print("female", mentor.numof_F)
        print("Asia (East)", mentor.asia_east)
        print("Europe (Western)", mentor.europe_western)
        print("North America", mentor.north_america)
        print("Asia (Central/South)", mentor.asia_central_south)
        print("Central/South America", mentor.central_south_america)
        print("Middle East/North Africa", mentor.middle_east_north_africa)
        print("Africa", mentor.africa)
        print("Europe (Eastern)",mentor.europe_eastern)
        print("Oceania", mentor.oceania)
        print("Asia (Central/South) / Middle East", mentor.asia_central_south_middle_east)
        total += mentor.group_size
    return total

def sortMentors():
    MENTORS.sort(key=lambda mentor: mentor.iteration)
    MENTORS.sort(key=lambda mentor: mentor.group_size)


def checkRegion(mentor: Mentor, mentee: Mentee):
    if mentee.region == "Asia (East)":
        mentor.asia_east += 1
    elif mentee.region == "Europe (Western)":
        mentor.europe_western += 1
    elif mentee.region == "North America":
        mentor.north_america  += 1
    elif mentee.region == "Asia (Central/South)":
        mentor.asia_central_south += 1
    elif mentee.region == "Central/South America":
        mentor.central_south_america += 1
    elif mentee.region == "Middle East/North Africa":
        mentor.middle_east_north_africa += 1
    elif mentee.region == "Africa":
        mentor.africa += 1
    elif mentee.region == "Europe (Eastern)":
        mentor.europe_eastern += 1
    elif mentee.region == "Oceania":
        mentor.oceania += 1
    elif mentee.region == "Asia (Central/South) / Middle East":
        mentor.asia_central_south_middle_east += 1
    else:
        mentor.other_cont += 1




def mentorNames():
    mentorsPrint = list()
    for mentor in MENTORS:
        mentorsPrint.append(mentor.name + " " +
                            str(mentor.group_size))

    print(mentorsPrint)



def assignMenteesAhmad():
    # sort mentees by country of residence alphabetically
    MENTEES.sort(key=lambda mentee: mentee.country_single)

    # sort mentees by region of residence alphabetically
    MENTEES.sort(key=lambda mentee: mentee.region)

    menteeNum = 0
    i = 0
    for mentee in MENTEES:
        gender = mentee.gender
        country = mentee.country_single
        # restart counter based on num of mentors
        i = 0
        current_mentor = MENTORS[i]
        # conditions to skip mentors
        mentors_skipped = 0
        iterations = 0
        # Summer Contact
        while current_mentor.name == mentee.summer_contact:
            i = i + 1
            # restart counter based on num of mentors
            if i == 27:
                i = 0
            current_mentor = MENTORS[i]
            mentors_skipped += 1
            iterations += 1
            # if none of the groups have room, use current index
            if iterations > 27:
                break
        # Same Country
        while current_mentor.country == country:
            i = i + 1
            # restart counter based on num of mentors
            if i == 27:
                i = 0
            current_mentor = MENTORS[i]
            mentors_skipped += 1
            iterations += 1
            # if none of the groups have room, use current index
            if iterations > 27:
                break
        iterations = 0
        while current_mentor.group_size == 11:
            i = i + 1
            # restart counter based on num of mentors
            if i == 27:
                i = 0
            current_mentor = MENTORS[i]
            iterations += 1
            # if none of the groups have room, use current index
            if iterations > 27:
                break
        iterations = 0
        while current_mentor.numof_F >= 6 and gender == 'Female':
            i = i + 1
            # restart counter based on num of mentors
            if i == 27:
                i = 0
            current_mentor = MENTORS[i]
            mentors_skipped += 1
            iterations += 1
            # if none of the groups have room, use current index
            if iterations > 27:
                break
        iterations = 0
        while current_mentor.numof_M >= 6 and gender == 'Male':
            i = i + 1
            # restart counter based on num of mentors
            if i == 27:
                i = 0
            current_mentor = MENTORS[i]
            mentors_skipped += 1
            iterations += 1
            # if none of the groups have room, use current index
            if iterations > 27:
                break


        if menteeNum > 260:
            mentorNames()
        MENTORS[i].mentees.append(mentee)
        MENTORS[i].iteration = menteeNum
        menteeNum += 1
        MENTORS[i].group_size += 1
        if gender == "Male":
            MENTORS[i].numof_M += 1
        elif gender == "Female":
            MENTORS[i].numof_F += 1
        else:
            MENTORS[i].numof_Other += 1

        checkRegion(MENTORS[i], mentee)
        sortMentors()


def write_file(filename: str, mentor_group: Mentor):
    """
    Method writes a mentor group infromation in seperate rows
    :param filename: name of the file to write in
    :param mentor_group: is the mentor group to write into this file
    :return:
    """
    file_to_write = open(filename, "w", newline='')
    writer = csv.writer(file_to_write)

    writer.writerow(["Last Name", "First Name",
                    "Preferred Name", "Pronouns",
                    "Brown Email", "Alt Email",
                    "Citizenships", "Student Type",
                    "SummerContact", "Mentor Name"])
    for mentee in mentor_group.mentees:
        writer.writerow([mentee.last_name, mentee.first_name,
                         mentee.preferred_name, mentee.pronouns,
                         mentee.brown_email, mentee.alt_email, 
                         mentee.citizenships, mentee.student_type, 
                         mentee.summer_contact, 
                         mentor_group.name])

    file_to_write.close()


def write_all_files():
    '''Writes all files for 25 mentors'''
    index = 1
    for mentor in MENTORS:
        write_file("MentorSheets/" + mentor.name + ".csv", mentor)
        index += 1

# write onne workbook






parse_mentees("mentees.csv")
parse_mentors("mentors.csv")
assignMenteesAhmad()
write_all_files()

# # https://stackoverflow.com/questions/51964001/merging-multiple-csv-files-into-separate-tabs-of-a-spreadsheet-in-python
# path = "Mentor Sheets"
# all_files = glob.glob(os.path.join(path, "*.csv"))
# writer = pd.ExcelWriter('Mentor Groups.xlsx', engine='xlsxwriter')
# for f in all_files:
#     df = pd.read_csv(f)
#     df.to_excel(writer, sheet_name=os.path.basename(f))

# writer.save()

#print(total_students_assigned())
#print(MENTORS)