# Assignment No. 1
class Country(object):
    def __init__(self,country_name,country_code):
        self.country_name = country_name
        self.country_code = country_code
    
    def __str__(self):
        return self.country_name + ", " +str(self.country_code)

    def getCountryCode(self):
        return self.country_code
       
    def getCountryName(self):
        return self.country_name

class Person(object):
    def __init__(self,student_number,first_name,last_name,gender,occupation,country_code,area_code,phone_number):
        self.student_number = student_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.occupation = occupation
        self.area_code = area_code
        self.country_code = country_code
        self.phone_number = phone_number

    def __str__(self):
        return self.student_number+", "+self.first_name+", "+self.last_name+", "+self.gender+", "+self.occupation+", "+self.area_code+", "+self.country_code+", "+self.phone_number
        
    def updateStudentNumber(self, newStudentNumber):
        self.student_number = newStudentNumber

    def updateFirstName(self, newFirstName):
        self.first_name = newFirstName

    def updateLastName(self, newLastName):
        self.last_name = newLastName
        
    def updateGender(self, newGender):
        self.gender = newGender

    def updateOccupation(self, newOccupation):
        self.occupation = newOccupation

    def updateAreaCode(self, newAreaCode):
        self.area_code = newAreaCode
        
    def updateCountryCode(self, newCountryCode):
        self.country_code = newCountryCode
        
    def updatePhonNumber(self, newPhoneNumber):
        self.phone_number = newPhoneNumber

    def getStudentNumber(self):
        return self.student_number

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name
        
    def getGender(self):
        return self.gender

    def getOccupation(self):
        return self.occupation

    def getAreaCode(self):
        return self.area_code
        
    def getCountryCode(self):
        return self.country_code
       
    def getPhonNumber(self):
        return self.phone_number

class ASEANPhoneBook(object):
    def __init__(self,entries,filtered_data):
        self.entries = entries
        self.filtered_data = filtered_data
    
    def searchByStudentNumber(self,student_number):
        for index in range(len(self.entries)):
            if self.entries[index].getStudentNumber() == student_number: 
                return index
        return -1
    
    def editStudentEntry(self,student_number,attribute,new_data):
        for index in range(len(self.entries)):
            if self.getEntries()[index].getStudentNumber() == student_number:
                if attribute == 1:
                    self.getEntries()[index].updateStudentNumber(new_data)
                elif attribute == 2:
                    self.getEntries()[index].updateLastName(new_data)
                elif attribute == 3:
                    self.getEntries()[index].updateGender(new_data)
                elif attribute == 4:
                    self.getEntries()[index].updateOccupation(new_data)
                elif attribute == 5:
                    self.getEntries()[index].updateCountryCode(new_data)
                elif attribute == 6:
                    self.getEntries()[index].updateAreaCode(new_data)
                elif attribute == 7:
                    self.getEntries()[index].updatePhonNumber(new_data)

    def addStudentEntry(self,new_entry):
        self.entries.append(new_entry)

    def getEntries(self):
        return self.entries

    def setFilteredData(self,new_entry):
        self.filtered_data.append(new_entry)
    
    def getFilteredData(self):
        return self.filtered_data

phonebook = ASEANPhoneBook([],[])
country_book = []
data_prompts = []

country = ["Federation of Malaysia","Republic of Indonesia","Republic of the Philippines","Republic of Singapore","Kingdom of Thailand"]
codes = [60,62,63,65,66]

i = 0
while i < 5:
    country_book.append(Country(country[i],codes[i]))
    i+=1

read_phonebook = True
while read_phonebook == True:
   
    print("[1] Store to ASEAN phonebook","[2] Edit entry in ASEAN phonebook","[3] Search ASEAN phonebook by country", "[4] Exit", sep="\n" )
    option = int(input())

    if option == 1:
        print("option 1")
        data_prompts = ["Enter student number:", "Enter surname:", "Enter first name:", "Enter gender:", "Enter occupation:", "Enter country code:", "Enter area code:", "Enter phone number:", "Do you want to enter another entry [Y/N]?"]

        new_student_data = []
        data_index = 0

        create_new_entry = True
        while data_index < len(data_prompts) and create_new_entry == True:
            print(data_prompts[data_index])
            new_student_data.append(input())

            if data_index == len(data_prompts)-1:
                phonebook.addStudentEntry(Person(new_student_data[0],new_student_data[2],new_student_data[1],new_student_data[3],new_student_data[4],new_student_data[5],new_student_data[6],new_student_data[7]))
                
                if new_student_data[data_index] == 'Y':
                    data_index = 0
                    new_student_data = []
                    create_new_entry = True

                elif new_student_data[data_index] == 'N':
                    create_new_entry = False
                    break
            else:
                data_index += 1

        for i in range(len(phonebook.getEntries())):
            print(phonebook.getEntries()[i])
        
        read_phonebook = True

    elif option == 2:
        editing = True
        searching = True
        hit = False
        
        edit_entry,search_index = 0,0
        entry_index = -1

        data_prompts = ["Enter new student number:", "Enter new surname:", "Enter new gender:", "Enter new occupation:", "Enter new country code:", "Enter new area code:", "Enter new phone number:"]

        while searching == True:
            print("Enter student number:")
            search_param = input()

            for a in range(len(phonebook.getEntries())):
                print(phonebook.getEntries()[a])

            while search_index in range(len(phonebook.getEntries())):
                if phonebook.searchByStudentNumber(search_param) != -1:
                    entry_index = search_index
                    searching = False
                    hit = True
                    break
                else:
                    hit = False
                    search_index += 1
            
            if hit == True:
                while editing == True:

                    entry_index = phonebook.searchByStudentNumber(search_param)
                    print(phonebook.getEntries()[entry_index])

                    print("Here is the existing information about ",phonebook.getEntries()[entry_index].getStudentNumber(),":")
                    print(phonebook.getEntries()[entry_index].getFirstName(), phonebook.getEntries()[entry_index].getLastName(), "is a ",phonebook.getEntries()[entry_index].getOccupation(),". Phone number is ", phonebook.getEntries()[entry_index].getCountryCode(),"-",phonebook.getEntries()[entry_index].getAreaCode(),"-",phonebook.getEntries()[entry_index].getPhonNumber())

                    print("Which of the following information do you wish to change?")
                    print("[1] Student number [4] Occupation   [7] Phone Number","[2] Surname        [5] Country code [8] None - Back to Main Menu ","[3] Gender         [6] Area Code",sep="\n")
                    edit_entry = int(input())

                    if edit_entry == 8:
                        editing = False
                        searching = False
                    else:
                        print(data_prompts[edit_entry-1])
                        phonebook.editStudentEntry(search_param,edit_entry,input())
                        editing = True
            else:
                search_index = 0
                searching = True
                print("Student number does not exist in phonebook.")
            
        for b in range(len(phonebook.getEntries())):
            print(phonebook.getEntries()[b])
        
        read_phonebook = True
    elif option == 3:
        for b in range(len(phonebook.getEntries())):
            print(phonebook.getEntries()[b])

        filters = []
        searching_by_country = True
        
        i,choice = 1,-1

        print("[1] Philippines [2] Thailand [3] Singapore [4] Indonesia [5] Malaysia [6] ALL [0] No More")    
        
        while choice != 0:
            print("Enter choice", i)
            choice = int(input())
            
            if choice == 1:
                filters.append(int(country_book[2].getCountryCode()))
            elif choice == 2:
                filters.append(int(country_book[4].getCountryCode()))
            elif choice == 3:
                filters.append(int(country_book[3].getCountryCode()))
            elif choice == 4:
                filters.append(int(country_book[1].getCountryCode()))
            elif choice == 5:
                filters.append(int(country_book[0].getCountryCode()))
            elif choice == 6:
                filters = [int(country_book[0].getCountryCode()),int(country_book[1].getCountryCode()),int(country_book[2].getCountryCode()),int(country_book[3].getCountryCode()),int(country_book[4].getCountryCode())]
                break
            i += 1
        
        print(filters)

        filtered_data = []
        filtering = True
        
        phonebook_index = 0
        while phonebook_index in range(len(phonebook.getEntries())):
            filters_index = 0
            while filters_index in range(len(filters)):
                if int(phonebook.getEntries()[phonebook_index].getCountryCode()) == int(filters[filters_index]):
                    filtered_data.append(phonebook.getEntries()[phonebook_index])
                filters_index+=1
            phonebook_index+=1
        
        g=0
        for g in range(len(filtered_data)):
            print(filtered_data[g])

        if len(filtered_data) != 0:

            results_index = -1
            results_header = ""
            while results_index < 0:
                results_header += country_book[0].getCountryName()
                for index in range(1,len(filters)):
                    results_header += (" and " + country_book[index].getCountryName())
                print("Here are the students from ",results_header,end=".\n")
                results_index = 0

            count,sort_count,tag = 0,0,-1
            sort_data = []

            while count in range(len(filtered_data)):
                sort_data.append(filtered_data[count].getLastName()+"."+filtered_data[count].getStudentNumber())
                count+=1
            
            sort_data.sort()
            print(sort_data)

            while sort_count in range(len(sort_data)):
                student_number = sort_data[sort_count][sort_data[sort_count].index('.')+1:]
                for h in range(len(phonebook.getEntries())):
                    if phonebook.getEntries()[h].getStudentNumber() == student_number:
                        print(phonebook.getEntries()[h].getLastName(),", ",phonebook.getEntries()[h].getFirstName(),"with student number",phonebook.getEntries()[h].getStudentNumber()," is a",phonebook.getEntries()[h].getOccupation(),". Phone number is ",phonebook.getEntries()[h].getCountryCode(),"-",phonebook.getEntries()[h].getAreaCode(),"-",phonebook.getEntries()[h].getPhonNumber(),".")  
                sort_count+=1
        else:
            print("There are no phonebook entries from those countries.")

        read_phonebook = True
        
    else:
        print(option)
        read_phonebook = False