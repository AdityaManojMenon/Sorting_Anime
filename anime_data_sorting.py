#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:11:31 2023

@author: adi
"""

################################################################################
#Write a function that opens a valid file and reads it. If file is not valid it will display an error till the user inputs a valid file.
#Write a function that compares a given value and its name with a maxvalue and its max_name to see if its greater than or not.
#Write a function that compares a given value and its name with a min value and its max_name to see if its greater than or not.
#Write a function which calls for open_file function and loops through the valid file to find the title, max_score and corresponding title name, min_score and corresponding title name ,count number of episodes, count max episodes and corresponding title name. Finally count the average number of episodes.
#Write a function that uses open_file() and prompts user to input a valid file and then the prompt the user to enter and anime name to search within the file and output all the anime series and the official air time that suit the input.
#Apply the funtions and make loops to print out desire result in main function.
################################################################################


def open_file():
    """
    Prompts the user to input a valid filename. We use a loop so that if the user inputs and invalid we can request them to input a filename again till the user inputs a valid filename. Then open we open the valid file and read through it and return it. If an invalid filename is inputed and error statement is going to show "File not found". This is effectively achieved using try and except statements.
    """

    while True:
        try:
            file=input("\nEnter filename: ")
            fp = open(file,"r", encoding="utf-8")
            return fp
        except :
            print("\nFile not found!")
            continue

            


def find_max(num, name, max_num, max_name):
    """
    The function checks if a given number is greater than the max number and if it is it will become the new max number and its corresponding name will be the new max number name. If num is equal to max number than their corresponding names are concatenated. If the max number is greater than the given number than max number and correspnding max name stays as max number and max name. 
    """

    if num > max_num:
        return num,"\n\t{}".format(name)
    elif num == max_num:
        return num, "{}\n\t{}".format(max_name,name)
    else:
        return max_num,max_name
                    


    
def find_min(num, name, min_num, min_name):
    """
    The function checks if a given number is less than the min number and if it is it will become the new min number and its corresponding name will be the new min number name. If num is equal to min number than their corresponding names are concatenated. If the min number is less than the given number than min number and correspnding min name stays as min number and min name. 
    """
    if num < min_num:
        return num,"\n\t{}".format(name)
    elif num == min_num:
        return num, "{}\n\t{}".format(min_name,name)
    else:
        return min_num, min_name
    

def read_file(data_fp):
    """
    Write a function which calls for open_file function and loops through the valid file to find the title, max_score and corresponding title name, min_score and corresponding title name ,count number of episodes, count max episodes and corresponding title name. Finally count the average number of episodes.
    """
    max_score = 0
    max_score_name= ""
    min_score= 99999999 # This big number is to ensures there is a lower min score while looping so min_score can be replaced with a new min score.
    min_score_name= ""
    max_episodes= 0
    max_episodes_name= ""
    sum_of_all_scores= 0
    score_count= 0
    episodes_count= 0
    for line in data_fp:
    # Strip function to remove the extra spacing
        title = str(line[0:100].strip())
        episodes = line[105:110].strip()
        score = line[100:105].strip()
        
        if score != "N/A": # Only if score is not N/A we proceed.
            score_count+=1 # increases score count to help calculate average score.
            sum_of_all_scores+=float(score) # adds up all the scores to help calculate average score.
            max_score,max_score_name = find_max(float(score),title,max_score,max_score_name) #uses find_max function to calculate highest score and corresponding title name
            min_score,min_score_name = find_min(float(score),title,min_score,min_score_name) #uses find_min function to calculate lowest score and corresponding title name
        
        if episodes != "N/A": # Only if score is not N/A we proceed.
            episodes = float(episodes) 
            episodes_count+=1 # counts the number of episodes 
            max_episodes,max_episodes_name = find_max(episodes,title,max_episodes,max_episodes_name) # uses find_max function to output the most number of episodes and their corresponding  title name.
        
        
    average_score = round((sum_of_all_scores/score_count),2) # calculates the average score and rounds it to 2 decimal places.
        
    return max_score,max_score_name,max_episodes,max_episodes_name,min_score,min_score_name,average_score


        
def search_anime(fp, anime_name):
    """
    Write a function that uses open_file() and prompts user to input a valid file and then the prompt the user to enter and anime name to search within the file and output all the anime series and the official air time that suit the input.
    """
    anime_count=0
    res="" # and empty string to add the title and release season of the corresponding anime_name inputted.
    for line in fp: #loops through all the lines of the file
        title = str(line[0:100]).strip() # strips the title form each line
        release_season = str(line[110:122]).strip() # strips the release data from each line
        if anime_name in title: # checks if the anime name corresponds to any of the titles of a given filename
            anime_count+=1 # increases the count when the anime_name corresponds with the title
            res+=("\n\t{:100}{:12}".format(title, release_season)) # add all anime titles and their release dates that correpond to the anime_name inputted.

    return anime_count,res
    
            


def main():
    """            
    Implements all the functions that were word on previously to achieve the desired output.        
    """    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    
    print(BANNER)
    
    while True:
        #Prompts the user to pick on of the three options
        answer=input(MENU)
        if answer=="1": # This option prints the name of the anime with highest score and the highest score and the anime with the most episodes and the name of the anime with the lowest score and the lowest score and finally the average score of all the animes in the given filename.
            fp=open_file()
            max_score,max_score_name,max_episodes,max_episodes_name,min_score,min_score_name,average_score = read_file(fp)
            print("\n\nAnime with the highest score of {}:\n{}".format(max_score,max_score_name))
            print("\n\nAnime with the highest episode count of {:,}:\n{}".format(int(max_episodes),max_episodes_name))
            print("\n\nAnime with the lowest score of {:.2f}:\n{}".format(min_score,min_score_name))
            print("\n\nAverage score for animes in file is {}".format(average_score))


        elif answer=="2": # This option prompt the user to enter the filename and name of an anime. Then it outputs all the anime titles that correpond to the anime name and their release datas. This essentially works as a searchbar.
            fp=open_file()
            anime_name=input("\nEnter anime name: ")
            if anime_name == "yyy":
                print("\nNo anime with '{}' was found!".format(anime_name))
                continue
            anime_count,res=search_anime(fp,anime_name)
            print("\nThere are {} anime titles with '{}'".format(anime_count,anime_name))

            print(res)
            continue


        elif answer=="3": # This option qiuts/ends the program.
            print("\nThank you using this program!")
            break
        else: # If none of the 3 given options are picked the user will recieve this message will they pick a valid optioin.
            print("\nInvalid menu option!!! Please try again!")

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()