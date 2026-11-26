"""
Name pools for diverse cultural, linguistic, and national traditions worldwide.
Provides authentic male, female, and unisex first names, as well as surnames.
"""

from typing import Dict, List, TypedDict


class NamePool(TypedDict):
    male_first: List[str]
    female_first: List[str]
    last_names: List[str]


NAME_POOLS: Dict[str, NamePool] = {
    # 1. Bangladesh
    "bangladeshi": {
        "male_first": [
            "Tanvir", "Shakib", "Rahim", "Karim", "Arafat", "Tamim", "Sabbir", "Mushfiq",
            "Mahmudullah", "Farhan", "Nasir", "Naim", "Jisan", "Anik", "Nayeem", "Tariq",
            "Zahid", "Shohel", "Siam", "Alamin", "Hasan", "Rifat", "Mehedi", "Fahim",
            "Ashiq", "Jahid", "Saiful", "Imran", "Arif", "Shanto", "Mustafiz", "Taskin"
        ],
        "female_first": [
            "Nusrat", "Sadia", "Jannat", "Farhana", "Tanzila", "Rima", "Mim", "Afsana",
            "Tasnim", "Sharmin", "Sabrina", "Rumana", "Shirin", "Nabila", "Sumaiya", "Lamia",
            "Anika", "Mehnaz", "Sultana", "Faria", "Samira", "Tahmina", "Marufa", "Priya",
            "Lubna", "Nasrin", "Tamanna", "Rokeya", "Naznin", "Munira", "Jahanara", "Sanjida"
        ],
        "last_names": [
            "Ahmed", "Hasan", "Rahman", "Islam", "Hossain", "Chowdhury", "Khan", "Ali",
            "Uddin", "Mia", "Sikder", "Bhuiyan", "Mollah", "Talukder", "Sarker", "Howlader",
            "Mazumder", "Akter", "Begum", "Dewan", "Kazi", "Majumder", "Gazi", "Biswas"
        ],
    },

    # 2. India
    "indian": {
        "male_first": [
            "Aarav", "Vihaan", "Aditya", "Rohan", "Kabir", "Aryan", "Reyansh", "Arjun",
            "Vivaan", "Dhruv", "Sai", "Ishaan", "Ayush", "Rahul", "Amit", "Vikram",
            "Sanjay", "Rajesh", "Karan", "Manish", "Deepak", "Naveen", "Pranav", "Gaurav"
        ],
        "female_first": [
            "Aanya", "Diya", "Saanvi", "Ananya", "Ishita", "Aarohi", "Pooja", "Priya",
            "Kavya", "Sneha", "Neha", "Riya", "Shreya", "Tanvi", "Meera", "Aditi",
            "Anushka", "Deepika", "Sunita", "Swati", "Nandini", "Pallavi", "Divya", "Komal"
        ],
        "last_names": [
            "Sharma", "Verma", "Patel", "Singh", "Kumar", "Gupta", "Reddy", "Mehta",
            "Nair", "Iyer", "Rao", "Joshi", "Bose", "Banerjee", "Chatterjee", "Mukherjee",
            "Das", "Chopra", "Malhotra", "Kapoor", "Agarwal", "Bhatia", "Deshmukh", "Kulkarni"
        ],
    },

    # 3. Pakistan
    "pakistani": {
        "male_first": [
            "Muhammad", "Bilal", "Hamza", "Usman", "Zubair", "Haris", "Babar", "Shaheen",
            "Rizwan", "Fakhar", "Shadab", "Asif", "Faheem", "Imad", "Shoaib", "Shahid",
            "Tariq", "Waqas", "Noman", "Khurram", "Danish", "Salman", "Zeeshan", "Kamran"
        ],
        "female_first": [
            "Ayesha", "Fatima", "Zainab", "Maryam", "Hiba", "Mahnoor", "Hania", "Kinza",
            "Iqra", "Bushra", "Laiba", "Eman", "Sara", "Hira", "Madiha", "Sidra",
            "Rabia", "Khadija", "Aleena", "Noor", "Nimra", "Anum", "Saba", "Zunaira"
        ],
        "last_names": [
            "Khan", "Malik", "Chaudhry", "Butt", "Bhatti", "Sheikh", "Qureshi", "Abbasi",
            "Farooqi", "Siddiqui", "Mirza", "Baig", "Raza", "Gill", "Jutt", "Gondal",
            "Dar", "Mughal", "Awan", "Hashmi", "Shah", "Shahid", "Rehman", "Lodhi"
        ],
    },

    # 4. Anglo-Western (US, UK, Canada, Australia, NZ)
    "anglo_western": {
        "male_first": [
            "James", "William", "Oliver", "Noah", "Liam", "Benjamin", "Lucas", "Henry",
            "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Matthew", "Jackson", "David",
            "Joseph", "Samuel", "Sebastian", "Jack", "Owen", "Carter", "Wyatt", "John"
        ],
        "female_first": [
            "Emma", "Olivia", "Amelia", "Sophia", "Charlotte", "Ava", "Isabella", "Mia",
            "Evelyn", "Harper", "Camila", "Gianna", "Abigail", "Ella", "Emily", "Elizabeth",
            "Sofia", "Avery", "Scarlett", "Chloe", "Victoria", "Grace", "Zoey", "Penelope"
        ],
        "last_names": [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson",
            "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "Martin", "Lee", "Perez",
            "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
            "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen"
        ],
    },

    # 5. Germanic (Germany, Austria, Switzerland, Liechtenstein)
    "germanic": {
        "male_first": [
            "Lukas", "Leon", "Maximilian", "Felix", "Paul", "Jonas", "Elias", "Finn",
            "Noah", "Ben", "Niklas", "Tim", "David", "Julian", "Philipp", "Moritz",
            "Alexander", "Jan", "Florian", "Fabian", "Tobias", "Sebastian", "Stefan", "Markus"
        ],
        "female_first": [
            "Mia", "Emma", "Hannah", "Sofia", "Anna", "Emilia", "Lina", "Marie",
            "Lena", "Mila", "Lea", "Laura", "Clara", "Nele", "Johanna", "Lara",
            "Sarah", "Charlotte", "Frieda", "Ida", "Mathilda", "Greta", "Maja", "Paula"
        ],
        "last_names": [
            "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker",
            "Schulz", "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf",
            "Schröder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Krüger", "Hofmann", "Hartmann"
        ],
    },

    # 6. French (France, Monaco, Haiti, etc.)
    "french": {
        "male_first": [
            "Gabriel", "Léo", "Raphaël", "Arthur", "Louis", "Lucas", "Adam", "Jules",
            "Hugo", "Maël", "Liam", "Noah", "Paul", "Ethan", "Sacha", "Tom",
            "Gaspard", "Antoine", "Clément", "Mathéo", "Victor", "Maxime", "Alexandre", "Enzo"
        ],
        "female_first": [
            "Jade", "Louise", "Emma", "Ambre", "Alice", "Rose", "Anna", "Mila",
            "Romy", "Mia", "Lina", "Chloé", "Léa", "Léna", "Manon", "Juliette",
            "Inès", "Camille", "Agathe", "Zoé", "Jeanne", "Lucie", "Eva", "Sarah"
        ],
        "last_names": [
            "Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois",
            "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David",
            "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine"
        ],
    },

    # 7. Hispanic Latin America & Spain
    "hispanic_latam": {
        "male_first": [
            "Mateo", "Santiago", "Matías", "Sebastián", "Diego", "Emiliano", "Nicolás", "Alejandro",
            "Lucas", "Benjamín", "Joaquín", "Leonardo", "Samuel", "Daniel", "Gabriel", "Tomás",
            "Thiago", "Carlos", "Javier", "Fernando", "Rodrigo", "Andrés", "Manuel", "Ángel"
        ],
        "female_first": [
            "Sofía", "Valentina", "Isabella", "Camila", "Valeria", "Mariana", "Gabriela", "Lucía",
            "Martina", "Victoria", "Elena", "Daniela", "Catalina", "Natalia", "Renata", "Paula",
            "Juana", "Antonella", "Samantha", "Ximena", "Andrea", "Fernanda", "Carolina", "Sara"
        ],
        "last_names": [
            "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez",
            "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Diaz", "Moreno", "Álvarez",
            "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos"
        ],
    },

    # 8. Brazilian (Lusophone South America)
    "brazilian": {
        "male_first": [
            "Miguel", "Arthur", "Heitor", "Bernardo", "Théo", "Davi", "Gabriel", "Pedro",
            "Samuel", "Lorenzo", "Benjamin", "Matheus", "Lucas", "Nicolas", "Joaquim", "Henrique",
            "Rafael", "Guilherme", "Murilo", "Felipe", "Gustavo", "Enzo", "Vitor", "Eduardo"
        ],
        "female_first": [
            "Helena", "Alice", "Laura", "Manuela", "Valentina", "Sophia", "Isabella", "Heloísa",
            "Luiza", "Júlia", "Lorena", "Lívia", "Maria Luiza", "Cecília", "Eloá", "Giovanna",
            "Maria Eduarda", "Mariana", "Lara", "Beatriz", "Antonella", "Emanuelly", "Isadora", "Melissa"
        ],
        "last_names": [
            "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira",
            "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes",
            "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Nascimento", "Andrade"
        ],
    },

    # 9. Italian (Italy, San Marino, Vatican, Malta)
    "italian": {
        "male_first": [
            "Leonardo", "Francesco", "Alessandro", "Lorenzo", "Mattia", "Andrea", "Gabriele", "Riccardo",
            "Tommaso", "Edoardo", "Federico", "Matteo", "Diego", "Niccolò", "Davide", "Giuseppe",
            "Pietro", "Antonio", "Samuele", "Filippo", "Marco", "Giovanni", "Luca", "Christian"
        ],
        "female_first": [
            "Sofia", "Aurora", "Giulia", "Ginevra", "Beatrice", "Alice", "Vittoria", "Emma",
            "Ludovica", "Matilde", "Giorgia", "Chiara", "Anna", "Camilla", "Greta", "Elena",
            "Francesca", "Sara", "Nicole", "Martina", "Bianca", "Noemi", "Gaia", "Alessia"
        ],
        "last_names": [
            "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci",
            "Marino", "Greco", "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa",
            "Giordano", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani"
        ],
    },

    # 10. Japanese
    "japanese": {
        "male_first": [
            "Haruto", "Yuto", "Sota", "Yuki", "Hayato", "Haruki", "Ryota", "Kaito",
            "Ren", "Takumi", "Daiki", "Kenji", "Kazuki", "Riku", "Taichi", "Shota",
            "Hinata", "Kota", "Naoki", "Sho", "Tsubasa", "Yuma", "Itsuki", "Shin"
        ],
        "female_first": [
            "Yui", "Aoi", "Hina", "Rin", "Sakura", "Yuna", "Miyu", "Nanami",
            "Akari", "Mei", "Kanna", "Koharu", "Sora", "Honoka", "Mao", "Rio",
            "Hiyori", "Saki", "Ayaka", "Misaki", "Asuka", "Nana", "Hikari", "Riko"
        ],
        "last_names": [
            "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura",
            "Kobayashi", "Kato", "Yoshida", "Yamada", "Sasaki", "Yamaguchi", "Saito", "Matsumoto",
            "Inoue", "Kimura", "Hayashi", "Shimizu", "Yamazaki", "Mori", "Abe", "Ikeda"
        ],
    },

    # 11. Chinese (China, Taiwan, Singapore)
    "chinese": {
        "male_first": [
            "Wei", "Hao", "Yi", "Chen", "Jun", "Jian", "Bo", "Lei",
            "Tao", "Qiang", "Peng", "Ming", "Chao", "Zhen", "Feng", "Jie",
            "Long", "Xiang", "Kai", "Rui", "Yang", "Bin", "Yu", "Hui"
        ],
        "female_first": [
            "Fang", "Xiu", "Ying", "Min", "Jing", "Li", "Yan", "Dan",
            "Na", "Ping", "Ting", "Ling", "Mei", "Lan", "Hong", "Qian",
            "Xin", "Yue", "Jia", "Meng", "Xue", "Yun", "Fei", "Shu"
        ],
        "last_names": [
            "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao",
            "Wu", "Zhou", "Xu", "Sun", "Ma", "Zhu", "Hu", "Guo",
            "He", "Gao", "Lin", "Luo", "Zheng", "Liang", "Xie", "Song"
        ],
    },

    # 12. Korean (South & North Korea)
    "korean": {
        "male_first": [
            "Min-jun", "Seo-jun", "Do-yun", "Ye-jun", "Si-woo", "Ha-joon", "Ji-ho", "Ju-won",
            "Jun-woo", "Ji-hoon", "Hyun-woo", "Geon-woo", "Woo-jin", "Sun-woo", "Eun-woo", "Jung-hoon",
            "Tae-hyung", "Jungkook", "Ji-min", "Nam-joon", "Min-ho", "Seung-gi", "Jin-woo", "Dong-hyun"
        ],
        "female_first": [
            "Seo-yeon", "Seo-yun", "Ji-woo", "Seo-hyeon", "Min-seo", "Ha-eun", "Ha-yoon", "Yun-seo",
            "Ji-min", "Ji-yu", "Chae-won", "Su-a", "Da-eun", "Ye-eun", "Soo-bin", "Eun-ji",
            "Ji-eun", "Na-yeon", "Yoo-na", "Bo-ra", "Hye-jin", "Min-ji", "Sun-hee", "Yoo-jung"
        ],
        "last_names": [
            "Kim", "Lee", "Park", "Choi", "Jeong", "Kang", "Cho", "Yoon",
            "Jang", "Lim", "Han", "Oh", "Seo", "Shin", "Kwon", "Hwang",
            "Ahn", "Song", "Ryu", "Hong", "Ko", "Moon", "Yang", "Son"
        ],
    },

    # 13. Russian & East Slavic (Russia, Ukraine, Belarus)
    "east_slavic": {
        "male_first": [
            "Alexander", "Mikhail", "Ivan", "Dmitry", "Sergey", "Andrey", "Alexey", "Artem",
            "Maxim", "Ilya", "Vladimir", "Pavel", "Nikita", "Denis", "Roman", "Anton",
            "Vladislav", "Egor", "Kirill", "Yaroslav", "Timofey", "Matvey", "Konstantin", "Viktor"
        ],
        "female_first": [
            "Anastasia", "Maria", "Daria", "Anna", "Elena", "Olga", "Ekaterina", "Polina",
            "Alisa", "Victoria", "Ksenia", "Svetlana", "Yulia", "Natalia", "Irina", "Tatiana",
            "Sofia", "Veronika", "Margarita", "Valeria", "Alena", "Kristina", "Eva", "Diana"
        ],
        "last_names": [
            "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Vasiliev", "Petrov", "Sokolov", "Mikhailov",
            "Novikov", "Fedorov", "Morozov", "Volkov", "Alekseev", "Lebedev", "Semenov", "Egorov",
            "Pavlov", "Kozlov", "Stepanov", "Nikolaev", "Orlov", "Andreev", "Makarov", "Nikitin"
        ],
    },

    # 14. Turkish (Turkey)
    "turkish": {
        "male_first": [
            "Yusuf", "Eymen", "Ömer", "Miraç", "Kerem", "Mustafa", "Ahmet", "Mehmet",
            "Ali", "Emir", "Eren", "Alparslan", "Hamza", "Burak", "Emre", "Can",
            "Deniz", "Kaan", "Barış", "Arda", "Tolga", "Mert", "Oğuz", "Serkan"
        ],
        "female_first": [
            "Zeynep", "Elif", "Defne", "Asra", "Ebrar", "Eylül", "Miray", "Zehra",
            "Azra", "Nehir", "Fatma", "Ayşe", "Meryem", "Ceren", "Dilara", "Selin",
            "Gamze", "Melis", "Damla", "Gizem", "İrem", "Ece", "Büşra", "Yağmur"
        ],
        "last_names": [
            "Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Yıldız", "Yıldırım", "Öztürk",
            "Aydın", "Özdemir", "Arslan", "Doğan", "Kılıç", "Aslan", "Çetin", "Kara",
            "Koç", "Kurt", "Özkan", "Şimşek", "Polat", "Özcan", "Korkmaz", "Erdoğan"
        ],
    },

    # 15. Gulf Arabic (Saudi, UAE, Qatar, Kuwait, Bahrain, Oman, Yemen)
    "gulf_arabic": {
        "male_first": [
            "Mohammed", "Abdullah", "Fahad", "Khalid", "Sultan", "Abdulaziz", "Saud", "Hamad",
            "Nasser", "Faisal", "Bandar", "Rashid", "Mansour", "Majed", "Turki", "Salem",
            "Tariq", "Zayed", "Mubarak", "Saad", "Nayef", "Bader", "Waleed", "Talal"
        ],
        "female_first": [
            "Nourah", "Sara", "Reem", "Lulwah", "Hessa", "Maha", "Latifa", "Fatima",
            "Alanood", "Deema", "Dana", "Jawaher", "Shaikha", "Maryam", "Munira", "Ghada",
            "Mashael", "Abeer", "Wafa", "Asma", "Rawan", "Hala", "Dalal", "Budoor"
        ],
        "last_names": [
            "Al-Otaibi", "Al-Ghamdi", "Al-Harbi", "Al-Shehri", "Al-Dossari", "Al-Zahrani", "Al-Qahtani", "Al-Mutairi",
            "Al-Subaie", "Al-Shammari", "Al-Rashidi", "Al-Hajri", "Al-Marri", "Al-Nuaimi", "Al-Falasi", "Al-Ketbi",
            "Al-Mansouri", "Al-Kaabi", "Al-Suwaidi", "Al-Kuwari", "Al-Sabah", "Al-Thani", "Al-Nahyan", "Al-Maktoum"
        ],
    },

    # 16. Egyptian Arabic (Egypt, Sudan)
    "egyptian_arabic": {
        "male_first": [
            "Ahmed", "Mohamed", "Mahmoud", "Mostafa", "Omar", "Amr", "Tamer", "Karim",
            "Youssef", "Hassan", "Hussein", "Sherif", "Sameh", "Hazem", "Mazen", "Ziad",
            "Essam", "Wael", "Ayman", "Khaled", "Ibrahim", "Tariq", "Hani", "Eslam"
        ],
        "female_first": [
            "Mariam", "Fatma", "Nour", "Salma", "Aya", "Sara", "Heba", "Rania",
            "Dina", "Mona", "Menna", "Nada", "Yasmin", "Mai", "Noha", "Hadeer",
            "Radwa", "Amira", "Donia", "Esraa", "Nadine", "Farida", "Engy", "Reham"
        ],
        "last_names": [
            "El-Sayed", "Abdel-Rahman", "Ibrahim", "Hassan", "Ali", "Mahmoud", "Mostafa", "Soliman",
            "Fahmy", "Khalil", "Salama", "Mansour", "El-Masry", "Badawy", "Ghoneim", "Naguib",
            "Othman", "Shafik", "Farouk", "El-Naggar", "Shalaby", "Metwally", "Radwan", "El-Baz"
        ],
    },

    # 17. Maghreb Arabic (Morocco, Algeria, Tunisia, Libya, Mauritania)
    "maghreb_arabic": {
        "male_first": [
            "Youssef", "Amine", "Mehdi", "Hamza", "Ayoub", "Anas", "Rayane", "Ilyas",
            "Walid", "Reda", "Karim", "Bilal", "Sofiane", "Adel", "Tarik", "Nassim",
            "Samir", "Zouhair", "Rachid", "Hicham", "Mourad", "Nabil", "Brahim", "Fouad"
        ],
        "female_first": [
            "Imane", "Salma", "Hajar", "Khadija", "Fatima-Zahra", "Zineb", "Soukaina", "Meryem",
            "Chaimae", "Nour", "Manal", "Asmaa", "Ines", "Yasmine", "Siham", "Kenza",
            "Nawal", "Houda", "Leila", "Samira", "Sabrina", "Bouchra", "Hasna", "Latifa"
        ],
        "last_names": [
            "Benali", "Bennani", "El-Idrissi", "El-Amrani", "Mansouri", "Bouazza", "Berrada", "Tazi",
            "Alaoui", "Chraibi", "Belkacem", "Brahimi", "Guerrouj", "Saidi", "Haddad", "Cherif",
            "Benmoussa", "Benkirane", "Belhadj", "Zitouni", "Dahmani", "Amara", "Chaouch", "Khelifi"
        ],
    },

    # 18. Levant Arabic (Lebanon, Syria, Jordan, Iraq, Palestine)
    "levant_arabic": {
        "male_first": [
            "Jad", "Charbel", "Elie", "Sami", "Karim", "Ziad", "Fadi", "Rami",
            "Tarek", "Wassim", "Bassam", "Nizar", "Ghassan", "Firas", "Hani", "Samer",
            "Ahmad", "Mahmoud", "Laith", "Zaid", "Bashar", "Hatem", "Marwan", "Jamil"
        ],
        "female_first": [
            "Nour", "Lara", "Maya", "Tala", "Reem", "Zeina", "Lina", "Rana",
            "Yara", "Hala", "Dima", "Lynn", "Jana", "Mira", "Rita", "Celine",
            "Nadine", "Rania", "Salma", "Rawan", "Dana", "Rima", "Shirine", "Ghalia"
        ],
        "last_names": [
            "Khoury", "Haddad", "Saab", "Gemayel", "Hariri", "Sleiman", "Aoun", "Salameh",
            "Nasser", "Al-Khatib", "Al-Masri", "Al-Husseini", "Bitar", "Najjar", "Barakat", "Shami",
            "Kassir", "Zahra", "Mroue", "Darwish", "Boulos", "Sarkis", "Farhat", "Abboud"
        ],
    },

    # 19. Persian & Afghan (Iran, Afghanistan, Tajikistan)
    "persian_afghan": {
        "male_first": [
            "Arash", "Kian", "Arman", "Reza", "Sohrab", "Farhad", "Babak", "Navid",
            "Sina", "Ramin", "Shahin", "Hossein", "Milad", "Behrouz", "Kourosh", "Dariush",
            "Ahmad", "Massoud", "Zia", "Yama", "Rohullah", "Mirwais", "Farid", "Jamshid"
        ],
        "female_first": [
            "Shirin", "Parisa", "Niloofar", "Roya", "Nazanin", "Maryam", "Sepideh", "Golnaz",
            "Anahita", "Taraneh", "Setareh", "Sahar", "Marjan", "Mitra", "Azadeh", "Laila",
            "Zarlasht", "Freshta", "Breshna", "Wagma", "Benafsha", "Khatira", "Tamana", "Spogmai"
        ],
        "last_names": [
            "Tehrani", "Shirazi", "Esfahani", "Hosseini", "Mohammadi", "Rezaei", "Moradi", "Ahmadi",
            "Karimi", "Rostami", "Ebrahimi", "Soltani", "Jafari", "Hashemi", "Afshar", "Pahlavi",
            "Wardak", "Popalzai", "Durrani", "Stanikzai", "Mohmand", "Shinwari", "Noorzai", "Hotak"
        ],
    },

    # 20. Nigerian (Nigeria)
    "nigerian": {
        "male_first": [
            "Chinedu", "Emeka", "Oluwaseun", "Babatunde", "Tobi", "Ifeanyi", "Chidi", "Femi",
            "Adeyemi", "Olumide", "Nnamdi", "Obinna", "Kelechi", "Chukwudi", "Kayode", "Ayodele",
            "Ibrahim", "Abubakar", "Musa", "Usman", "Aliyu", "Suleiman", "Sani", "Bello"
        ],
        "female_first": [
            "Chioma", "Ngozi", "Amaka", "Adanna", "Chiamaka", "Oluchi", "Funke", "Titilayo",
            "Yetunde", "Folashade", "Simisola", "Blessing", "Precious", "Mercy", "Faith", "Joy",
            "Zainab", "Fatima", "Amina", "Hauwa", "Halima", "Khadija", "Maryam", "Aisha"
        ],
        "last_names": [
            "Adeyemi", "Okonkwo", "Balogun", "Okafor", "Nwosu", "Adeleke", "Ogunleye", "Eze",
            "Onyekwere", "Bello", "Abubakar", "Danjuma", "Lawal", "Sanusi", "Mohammed", "Ibrahim",
            "Ojo", "Akintola", "Babangida", "Chukwu", "Nwachukwu", "Obi", "Omeh", "Ajayi"
        ],
    },

    # 21. West African Francophone (Senegal, Mali, Côte d'Ivoire, Cameroon, Benin, etc.)
    "west_african_franco": {
        "male_first": [
            "Mamadou", "Abdoulaye", "Ousmane", "Cheikh", "Bakary", "Modibo", "Souleymane", "Ibrahima",
            "Seydou", "Boubacar", "Amadou", "Moussa", "Sekou", "Adama", "Koffi", "Yao",
            "Didier", "Samuel", "Patrick", "Brice", "Arnaud", "Franck", "Hervé", "Gervais"
        ],
        "female_first": [
            "Fatou", "Awa", "Mariama", "Aminata", "Coumba", "Rokhayatou", "Khady", "Oumou",
            "Diarra", "Fanta", "Kadiatou", "Assitan", "Saran", "Aïcha", "Akissi", "Affoué",
            "Christelle", "Estelle", "Sandrine", "Murielle", "Clarisse", "Nathalie", "Béatrice", "Prisca"
        ],
        "last_names": [
            "Diallo", "Traoré", "Diop", "Sow", "Ba", "Ndiaye", "Touré", "Keïta",
            "Coulibaly", "Cissé", "Koné", "Sissoko", "Camara", "Barry", "Sylla", "Dramé",
            "Kouassi", "Koffi", "Yao", "Konan", "Bamba", "Ouattara", "Eto'o", "Song"
        ],
    },

    # 22. East African (Kenya, Tanzania, Uganda, Rwanda, etc.)
    "east_african": {
        "male_first": [
            "Juma", "Baraka", "Mwangi", "Otieno", "Kiprono", "Kipchoge", "Omondi", "Kamau",
            "Wanjala", "Kariuki", "Kiplagat", "Dennis", "Brian", "Kelvin", "Emmanuel", "Moses",
            "Kassim", "Hamisi", "Bakari", "Athumani", "Shaban", "Rashid", "Ally", "Faraji"
        ],
        "female_first": [
            "Achieng", "Atieno", "Wanjiku", "Nyambura", "Muthoni", "Chebet", "Cherono", "Wangari",
            "Wairimu", "Akinyi", "Adhiambo", "Faith", "Mercy", "Grace", "Joyce", "Brenda",
            "Amina", "Zuhura", "Rehema", "Subira", "Mwanaidi", "Fatuma", "Zainabu", "Saida"
        ],
        "last_names": [
            "Mwangi", "Kamau", "Ochieng", "Otieno", "Onyango", "Kipchirchir", "Kiptoo", "Kariuki",
            "Waweru", "Njoroge", "Maina", "Karanja", "Mugisha", "Uwase", "Kagame", "Gasana",
            "Massaquoi", "Ssemwogerere", "Mukasa", "Kato", "Bwambale", "Kintu", "Okello", "Otim"
        ],
    },

    # 23. Southern African (South Africa, Zimbabwe, Botswana, Namibia, Zambia)
    "southern_african": {
        "male_first": [
            "Sipho", "Bongani", "Thabo", "Sibusiso", "Mandla", "Lethabo", "Kagiso", "Tshepo",
            "Tendai", "Farai", "Tinashe", "Tatenda", "Blessing", "Gift", "Simba", "Tapiwa",
            "Luan", "Liam", "Junior", "Keanu", "Francois", "Johan", "Pieter", "Hendrik"
        ],
        "female_first": [
            "Nomvula", "Thandiwe", "Busisiwe", "Zanele", "Lerato", "Kgomotso", "Refilwe", "Nthabiseng",
            "Chiedza", "Ruvimbo", "Nyasha", "Tariro", "Rutendo", "Kudzanai", "Vimbai", "Precious",
            "Minke", "Anika", "Chané", "Elri", "Danielle", "Leandri", "Simoné", "Carla"
        ],
        "last_names": [
            "Dlamini", "Nkosi", "Ndlovu", "Khumalo", "Sithole", "Mthembu", "Ngcobo", "Zwane",
            "Moyo", "Sibanda", "Ncube", "Gumbo", "Mpofu", "Dube", "Nyathi", "Tshuma",
            "Van der Merwe", "Botha", "Pretorius", "Du Plessis", "Fourie", "Venter", "Coetzee", "Nel"
        ],
    },

    # 24. Nordic (Sweden, Norway, Denmark, Iceland)
    "nordic": {
        "male_first": [
            "Lucas", "Liam", "William", "Elias", "Noah", "Hugo", "Oliver", "Oscar",
            "Adam", "Filip", "Ludvig", "Axel", "Emil", "Leo", "Viktor", "Magnus",
            "Sander", "Henrik", "Sverre", "Haakon", "Mikkel", "Lasse", "Frederik", "Thor"
        ],
        "female_first": [
            "Alice", "Maja", "Elsa", "Astrid", "Wilma", "Freja", "Olivia", "Selma",
            "Alma", "Ella", "Ebba", "Signe", "Agnes", "Saga", "Nora", "Ingrid",
            "Hedda", "Emilie", "Ida", "Sofie", "Emma", "Frida", "Linnea", "Clara"
        ],
        "last_names": [
            "Andersson", "Johansson", "Karlsson", "Nilsson", "Eriksson", "Larsson", "Olsson", "Persson",
            "Svensson", "Gustafsson", "Hansen", "Johansen", "Olsen", "Larsen", "Andersen", "Pedersen",
            "Nielsen", "Jensen", "Møller", "Christensen", "Magnússon", "Jónsson", "Einarsson", "Gunnarsson"
        ],
    },

    # 25. Polish & West Slavic (Poland, Czechia, Slovakia)
    "west_slavic": {
        "male_first": [
            "Antoni", "Jan", "Aleksander", "Franciszek", "Jakub", "Szymon", "Mikołaj", "Filip",
            "Wojciech", "Stanisław", "Kacper", "Michał", "Piotr", "Tomasz", "Mateusz", "Krzysztof",
            "Jiří", "Jan", "Petr", "Josef", "Pavel", "Martin", "Jaroslav", "Miroslav"
        ],
        "female_first": [
            "Zuzanna", "Julia", "Zofia", "Maja", "Hanna", "Lena", "Alicja", "Maria",
            "Oliwia", "Amelia", "Wiktoria", "Aleksandra", "Natalia", "Karolina", "Katarzyna", "Paulina",
            "Eliška", "Anna", "Tereza", "Adéla", "Karolína", "Natálie", "Viktorie", "Kristýna"
        ],
        "last_names": [
            "Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński",
            "Szymański", "Woźniak", "Dąbrowski", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski", "Kwiatkowski",
            "Novák", "Svoboda", "Novotný", "Dvořák", "Černý", "Procházka", "Kučera", "Veselý"
        ],
    },

    # 26. Greek (Greece, Cyprus)
    "greek": {
        "male_first": [
            "Georgios", "Dimitrios", "Konstantinos", "Ioannis", "Nikolaos", "Panagiotis", "Vasileios", "Christos",
            "Athanasios", "Michail", "Spyridon", "Alexandros", "Petros", "Stavros", "Stylianos", "Evangelos",
            "Andreas", "Anastasios", "Theodoros", "Antonios", "Marios", "Ilias", "Sotirios", "Angelos"
        ],
        "female_first": [
            "Maria", "Eleni", "Aikaterini", "Vasiliki", "Sofia", "Angeliki", "Georgia", "Dimitra",
            "Konstantina", "Paraskevi", "Ioanna", "Evangelia", "Christina", "Panagiota", "Eirini", "Anna",
            "Despoina", "Stavroula", "Theodora", "Styliani", "Fotini", "Marina", "Alexandra", "Kalliopi"
        ],
        "last_names": [
            "Papadopoulos", "Oikonomou", "Georgiou", "Nikolaou", "Vasiliou", "Konstantinou", "Dimitriou", "Ioannou",
            "Papageorgiou", "Karagiannis", "Papanikolaou", "Vlachos", "Antoniou", "Alexiou", "Christodoulou", "Bakirtzis",
            "Stavrou", "Makris", "Giannakopoulos", "Petridis", "Lykos", "Spanos", "Diamantis", "Katsaros"
        ],
    },

    # 27. Filipino (Philippines)
    "filipino": {
        "male_first": [
            "Joshua", "Angelo", "John Mark", "Christian", "Mark Anthony", "Gabriel", "Nathaniel", "Daniel",
            "Justine", "Adrian", "Kenneth", "Jerome", "Francis", "Paolo", "Carlo", "Rafael",
            "Arnel", "Danilo", "Lito", "Bayani", "Datu", "Isagani", "Dakila", "Makisig"
        ],
        "female_first": [
            "Angel", "Princess", "Mary Joy", "Bea", "Nicole", "Althea", "Jasmine", "Kristine",
            "Marian", "Katrina", "Camille", "Rochelle", "Liza", "Janine", "Patricia", "Christine",
            "Mutya", "Mayumi", "Tala", "Diwata", "Luningning", "Malaya", "Marikit", "Dalisay"
        ],
        "last_names": [
            "Santos", "Reyes", "Cruz", "Bautista", "Del Rosario", "Gonzales", "Ramos", "Aquino",
            "Garcia", "Lopez", "Mendoza", "Castillo", "Villanueva", "Fernandez", "Torres", "De Leon",
            "Dela Cruz", "Tolentino", "Mercado", "Pascual", "Morales", "Flores", "Navarro", "Rivera"
        ],
    },

    # 28. Vietnamese (Vietnam)
    "vietnamese": {
        "male_first": [
            "Hùng", "Cường", "Dũng", "Nam", "Tuấn", "Minh", "Hoàng", "Long",
            "Đức", "Hải", "Phong", "Quân", "Sơn", "Trung", "Việt", "Bảo",
            "Thành", "Hiếu", "Tùng", "Khoa", "Phúc", "Khang", "Thịnh", "Trí"
        ],
        "female_first": [
            "Hoa", "Lan", "Mai", "Cúc", "Trang", "Hương", "Linh", "Thảo",
            "Hà", "Ngọc", "Phương", "Anh", "Quỳnh", "Thủy", "Hạnh", "Yến",
            "Nhi", "Vân", "Tâm", "Vy", "Châu", "Diệp", "Oanh", "Như"
        ],
        "last_names": [
            "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ",
            "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý",
            "Đào", "Đoàn", "Vương", "Trịnh", "Trương", "Đinh", "Lâm", "Phùng"
        ],
    },

    # 29. Indonesian & Malay (Indonesia, Malaysia, Brunei)
    "indonesian": {
        "male_first": [
            "Budi", "Agus", "Bambang", "Eko", "Joko", "Hendra", "Rizky", "Aditya",
            "Dimas", "Fajar", "Bayu", "Arif", "Wahyu", "Ilham", "Dedi", "Teguh",
            "Rian", "Prasetyo", "Surya", "Bintang", "Gilang", "Rafi", "Farhan", "Rangga"
        ],
        "female_first": [
            "Siti", "Sri", "Nur", "Dewi", "Putri", "Indah", "Rina", "Tri",
            "Lestari", "Maya", "Dian", "Ratna", "Ayu", "Fitri", "Wulandari", "Anggraini",
            "Nadia", "Sari", "Anisa", "Melati", "Kartika", "Tia", "Gita", "Dina"
        ],
        "last_names": [
            "Kusuma", "Pratama", "Wijaya", "Saputra", "Santoso", "Setiawan", "Utomo", "Nugroho",
            "Siregar", "Nasution", "Lubis", "Harahap", "Simanjuntak", "Hutapea", "Sitorus", "Panjaitan",
            "Suhendra", "Wibowo", "Hidayat", "Gunawan", "Susanto", "Purnomo", "Wahyudi", "Hermawan"
        ],
    },
    "malay": {
        "male_first": [
            "Muhammad", "Ahmad", "Amir", "Faizal", "Hafiz", "Hakim", "Irfan", "Khairul",
            "Luqman", "Nazmi", "Razak", "Shahril", "Syazwan", "Zulhilmi", "Danial", "Aiman"
        ],
        "female_first": [
            "Nurul", "Aina", "Farhana", "Fatin", "Izzati", "Nadia", "Natasha", "Suhana",
            "Syahirah", "Zalikha", "Anis", "Amira", "Safiyyah", "Hanis", "Balqis", "Maisarah"
        ],
        "last_names": [
            "bin Abdullah", "bin Ismail", "bin Othman", "bin Hassan", "bin Ibrahim", "bin Ahmad",
            "binti Abdullah", "binti Ismail", "binti Othman", "binti Hassan", "binti Ibrahim", "binti Ahmad"
        ],
    },

    # 30. Southeast Asian Thai & Lao
    "southeast_asian_thai_lao": {
        "male_first": [
            "Somchai", "Sompong", "Arthit", "Kittisak", "Natthanan", "Chaiwat", "Kittipong", "Anan",
            "Prasert", "Thanakorn", "Pichai", "Chatchai", "Piyawat", "Teerasil", "Sarawut", "Wichai"
        ],
        "female_first": [
            "Siriporn", "Kannika", "Patcharee", "Supaporn", "Warunee", "Ratana", "Narumon", "Sasithorn",
            "Chutima", "Pornthip", "Supaluck", "Wilaiwan", "Kanya", "Sunisa", "Nataya", "Pattama"
        ],
        "last_names": [
            "Saetang", "Saeliu", "Suksomboon", "Suksawat", "Rattanakorn", "Prasertkul", "Charoenwong",
            "Wongsuwan", "Boonme", "Chantaramongkol", "Srisuk", "Thongdee", "Rattanamanee", "Panyasiri"
        ],
    },

    # 31. Horn of Africa (Ethiopia, Eritrea, Somalia, Djibouti)
    "horn_african": {
        "male_first": [
            "Abebe", "Dawit", "Haile", "Yohannes", "Tewodros", "Kassahun", "Mulugeta", "Berhanu",
            "Abdi", "Mohamed", "Farah", "Guled", "Warsame", "Hassan", "Ali", "Liban"
        ],
        "female_first": [
            "Almaz", "Tigist", "Meseret", "Hiwot", "Genet", "Marta", "Bethlehem", "Selam",
            "Faduma", "Asha", "Halima", "Sahra", "Hodman", "Hodan", "Idil", "Filsan"
        ],
        "last_names": [
            "Bekele", "Tadesse", "Worku", "Alemu", "Kebede", "Desta", "Haile", "Girma",
            "Farah", "Warsame", "Gedi", "Shermarke", "Barre", "Osman", "Jama", "Egal"
        ],
    },

    # 32. South Slavic (Serbia, Croatia, Bosnia, Bulgaria, Montenegro, North Macedonia, Slovenia)
    "south_slavic": {
        "male_first": [
            "Luka", "Stefan", "Nikola", "Marko", "Miloš", "Aleksandar", "Dušan", "Lazar",
            "Ivan", "Filip", "Bojan", "Goran", "Zoran", "Petar", "Milan", "Dragan"
        ],
        "female_first": [
            "Milica", "Jelena", "Marija", "Ana", "Jovana", "Katarina", "Teodora", "Ivana",
            "Dunja", "Sara", "Tara", "Sofija", "Maja", "Bojana", "Dragana", "Snežana"
        ],
        "last_names": [
            "Jovanović", "Petrović", "Nikolić", "Ilić", "Đorđević", "Pavlović", "Marković", "Popović",
            "Stojanović", "Živković", "Horvat", "Kovačević", "Babić", "Marić", "Jurić", "Novak"
        ],
    },

    # 33. Hungarian (Hungary)
    "hungarian": {
        "male_first": [
            "Bence", "Máté", "Levente", "Noel", "Marcell", "Dániel", "Ádám", "Dávid",
            "Milán", "Áron", "Zsombor", "Botond", "Patrik", "Balázs", "Tamás", "Attila"
        ],
        "female_first": [
            "Hanna", "Anna", "Zoé", "Lili", "Emma", "Luca", "Zsófia", "Boglárka",
            "Jázmin", "Nóra", "Mira", "Laura", "Dorka", "Viktória", "Eszter", "Réka"
        ],
        "last_names": [
            "Nagy", "Kovács", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár",
            "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros"
        ],
    },

    # 34. Romanian & Moldovan
    "romanian": {
        "male_first": [
            "Andrei", "Alexandru", "Stefan", "David", "Mihai", "Ionut", "Gabriel", "Matei",
            "Cristian", "Florin", "Radu", "Bogdan", "Vlad", "Cosmin", "Adrian", "Daniel"
        ],
        "female_first": [
            "Maria", "Elena", "Ioana", "Andreea", "Alexandra", "Ana", "Stefania", "Gabriela",
            "Mihaela", "Daniela", "Alina", "Raluca", "Diana", "Bianca", "Roxana", "Laura"
        ],
        "last_names": [
            "Popa", "Radu", "Popescu", "Ionescu", "Nistor", "Constantin", "Stan", "Dumitru",
            "Gheorghe", "Dobre", "Marin", "Tudor", "Stoica", "Diaconu", "Munteanu", "Florea"
        ],
    },

    # 35. Finnish & Baltic
    "baltic_finnic": {
        "male_first": [
            "Eino", "Oliver", "Väinö", "Leo", "Elias", "Onni", "Venla", "Toivo",
            "Arturs", "Roberts", "Gustavs", "Jānis", "Mantas", "Matas", "Lukas", "Jokūbas"
        ],
        "female_first": [
            "Aino", "Sofia", "Helmi", "Ilona", "Emilia", "Aada", "Kerttu", "Linnea",
            "Emīlija", "Sofija", "Marta", "Alise", "Emilija", "Vilte", "Gabija", "Leja"
        ],
        "last_names": [
            "Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen", "Laine", "Koskinen",
            "Bērziņš", "Kalniņš", "Ozoliņš", "Jansons", "Kazlauskas", "Petrauskas", "Jankauskas", "Stankevičius"
        ],
    },
    "finnish": {
        "male_first": ["Eino", "Oliver", "Väinö", "Leo", "Elias", "Onni", "Ilmari", "Matias", "Lauri", "Antti"],
        "female_first": ["Aino", "Sofia", "Helmi", "Ilona", "Emilia", "Aada", "Kerttu", "Venla", "Siiri", "Sanni"],
        "last_names": ["Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen", "Laine", "Koskinen", "Heikkinen", "Järvinen"],
    },

    # 36. Celtic Irish
    "irish_celtic": {
        "male_first": [
            "Jack", "James", "Noah", "Daniel", "Conor", "Finn", "Liam", "Fionn",
            "Cillian", "Oisín", "Patrick", "Seán", "Cian", "Darragh", "Tadhg", "Callum"
        ],
        "female_first": [
            "Emily", "Grace", "Fiadh", "Sophie", "Hannah", "Amelia", "Ava", "Isla",
            "Freya", "Aoife", "Saoirse", "Caoimhe", "Ciara", "Niamh", "Róisín", "Sadhbh"
        ],
        "last_names": [
            "Murphy", "Kelly", "O'Brien", "Ryan", "O'Connor", "Walsh", "O'Sullivan", "McCarthy",
            "Byrne", "Doyle", "Lynch", "O'Neill", "Reilly", "Dunne", "Brennan", "Gallagher"
        ],
    },

    # 37. Iberian Portuguese (Portugal)
    "iberian_portuguese": {
        "male_first": [
            "Francisco", "Afonso", "João", "Tomás", "Duarte", "Lourenço", "Rodrigo", "Martim",
            "Santiago", "Tiago", "Miguel", "Gabriel", "Guilherme", "Lucas", "Salvador", "Gonçalo"
        ],
        "female_first": [
            "Maria", "Leonor", "Matilde", "Beatriz", "Carolina", "Mariana", "Ana", "Sofia",
            "Francisca", "Inês", "Margarida", "Clara", "Lara", "Laura", "Alice", "Benedita"
        ],
        "last_names": [
            "Silva", "Santos", "Ferreira", "Pereira", "Oliveira", "Costa", "Rodrigues", "Martins",
            "Jesus", "Sousa", "Fernandes", "Gonçalves", "Gomes", "Lopes", "Marques", "Alves"
        ],
    },

    # 38. Iberian Spanish (Spain, Andorra)
    "iberian_spanish": {
        "male_first": [
            "Hugo", "Mateo", "Martín", "Lucas", "Leo", "Daniel", "Alejandro", "Manuel",
            "Pablo", "Álvaro", "Adrián", "Enzo", "Mario", "Diego", "David", "Oliver"
        ],
        "female_first": [
            "Lucía", "Sofía", "Martina", "María", "Julia", "Paula", "Valeria", "Emma",
            "Daniela", "Carla", "Alba", "Noa", "Lola", "Claudia", "Carmen", "Sara"
        ],
        "last_names": [
            "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez",
            "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Diaz", "Moreno", "Álvarez"
        ],
    },

    # 39. Benelux (Netherlands, Belgium, Luxembourg, Suriname)
    "benelux": {
        "male_first": [
            "Noah", "Sem", "Liam", "Lucas", "Daan", "Finn", "Levi", "Milan",
            "Bram", "Mees", "Jesse", "Luuk", "Sam", "Thomas", "Lars", "Thijs"
        ],
        "female_first": [
            "Emma", "Mila", "Sophie", "Tess", "Julia", "Sara", "Zoë", "Evi",
            "Fenno", "Lieke", "Eva", "Noor", "Lotte", "Yara", "Liv", "Fleur"
        ],
        "last_names": [
            "De Jong", "Jansen", "De Vries", "Van de Berg", "Van Dijk", "Bakker", "Janssen", "Visser",
            "Smit", "Meijer", "De Boer", "Mulder", "De Groot", "Bos", "Vos", "Peters"
        ],
    },

    # 40. Hebrew (Israel)
    "hebrew": {
        "male_first": [
            "David", "Ariel", "Lavi", "Noam", "Uri", "Eitan", "Daniel", "Yehonatan",
            "Itamar", "Omer", "Yosef", "Ori", "Refael", "Ari", "Moshe", "Ido"
        ],
        "female_first": [
            "Tamar", "Maya", "Avigail", "Noa", "Sarah", "Ayala", "Yael", "Lia",
            "Ella", "Shira", "Adel", "Rom", "Roni", "Hila", "Nomi", "Tal"
        ],
        "last_names": [
            "Cohen", "Levi", "Mizrahi", "Peretz", "Biton", "Dahan", "Avraham", "Friedman",
            "Malka", "Azulay", "Katz", "Yosef", "David", "Amar", "Omer", "Shapiro"
        ],
    },

    # 41. Sri Lankan (Sri Lanka)
    "sri_lankan": {
        "male_first": [
            "Kasun", "Nuwan", "Dinesh", "Chamara", "Roshan", "Sanjaya", "Asanka", "Pradeep",
            "Lahiru", "Thilina", "Mahela", "Kumar", "Sanath", "Lasith", "Angelo", "Wanindu"
        ],
        "female_first": [
            "Dilani", "Nirosha", "Anoma", "Kavindi", "Sachini", "Tharushi", "Sanduni", "Chamari",
            "Oshadi", "Hiruni", "Niluka", "Priyanka", "Menaka", "Ishara", "Dinusha", "Malsha"
        ],
        "last_names": [
            "Perera", "Fernando", "Silva", "De Silva", "Jayawardena", "Rajapaksa", "Bandara", "Senanayake",
            "Dissanayake", "Wickramasinghe", "Gunasekara", "Karunaratne", "Mendis", "Herath", "Ranatunga", "Kumara"
        ],
    },

    # 42. Nepali (Nepal)
    "nepali": {
        "male_first": [
            "Aayush", "Bipin", "Bibek", "Suman", "Kiran", "Roshan", "Dipendra", "Pradeep",
            "Sagar", "Nirajan", "Santosh", "Ashish", "Anil", "Bikash", "Manoj", "Ramesh"
        ],
        "female_first": [
            "Sita", "Gita", "Pooja", "Aarati", "Sushma", "Bipana", "Sabina", "Sunita",
            "Manisha", "Alisha", "Samikshya", "Anjali", "Roshani", "Pramila", "Deepa", "Kabita"
        ],
        "last_names": [
            "Sharma", "Thapa", "Shrestha", "Adhikari", "Karki", "Rai", "Gurung", "Tamang",
            "Bhandari", "Basnet", "Magar", "Poudel", "Subedi", "Bhattarai", "Ghimire", "Dahal"
        ],
    },

    # 43. Caribbean Anglo (Jamaica, Bahamas, Barbados, Guyana, Trinidad, etc.)
    "caribbean_anglo": {
        "male_first": [
            "Usain", "Damian", "Kemar", "Jevaughn", "Andre", "Dwayne", "Sheldon", "Kevon",
            "Rohan", "Marlon", "Dwight", "Lennox", "Kofi", "Tevin", "Jamar", "Keron"
        ],
        "female_first": [
            "Shelly-Ann", "Shanice", "Sheniqua", "Tia", "Keisha", "Latoya", "Shantel", "Tamika",
            "Aaliyah", "Brianna", "Monique", "Shari", "Abigail", "Candice", "Rochelle", "Tanisha"
        ],
        "last_names": [
            "Campbell", "Brown", "Smith", "Johnson", "Williams", "Clarke", "Grant", "Gordon",
            "Morgan", "Powell", "Hylton", "Richards", "Francis", "Green", "Thompson", "Wright"
        ],
    },

    # 44. Central Asian Turkic (Kazakhstan, Uzbekistan, Kyrgyzstan, Turkmenistan, Azerbaijan)
    "central_asian_turkic": {
        "male_first": [
            "Alikhan", "Nurbol", "Timur", "Rustam", "Azamat", "Sanzhar", "Daniyar", "Erzhan",
            "Bekzod", "Jasur", "Otabek", "Shavkat", "Sardor", "Umid", "Farrukh", "Sherzod"
        ],
        "female_first": [
            "Aruzhan", "Madina", "Aigerim", "Ayazhan", "Dinara", "Kamila", "Zarina", "Gulzhan",
            "Sevara", "Nilufar", "Dilnoza", "Shahzoda", "Gulnora", "Feruza", "Malika", "Munisa"
        ],
        "last_names": [
            "Akhmetov", "Ospanov", "Kusainov", "Kim", "Aliev", "Suleimenov", "Ibragimov", "Nazarbaev",
            "Karimov", "Rahimov", "Tashpulatov", "Yusupov", "Khamidov", "Abdullaev", "Mirzayev", "Ismailov"
        ],
    },

    # 45. Pacific & Polynesian (Fiji, Samoa, Tonga, Kiribati, Micronesia, etc.)
    "pacific_polynesian": {
        "male_first": [
            "Sione", "Tevita", "Kelepi", "Tupou", "Taniela", "Inoke", "Paula", "Mosese",
            "Junior", "Malo", "Tavita", "Ioane", "Fa'a", "Latu", "Semisi", "Viliami"
        ],
        "female_first": [
            "Mele", "Ana", "Lupe", "Sina", "Tala", "Lina", "Elenoa", "Mere",
            "Salote", "Kasanita", "Fane", "Moana", "Lani", "Milika", "Adi", "Litiana"
        ],
        "last_names": [
            "Finau", "Tuipulotu", "Naufahu", "Veikoso", "Latu", "Fifita", "Taumalolo", "Vunipola",
            "Mata'afa", "Tuilagi", "Savea", "Nonu", "Koroibete", "Radradra", "Tuisova", "Kunatani"
        ],
    },

    # 46. Lusophone African (Angola, Mozambique, Cabo Verde, Guinea-Bissau, Sao Tome)
    "lusophone_african": {
        "male_first": [
            "Manuel", "António", "João", "José", "Francisco", "Afonso", "Edson", "Gelson",
            "Mário", "Helder", "Gilberto", "Paulo", "Valdemar", "Celso", "Euclides", "Mauro"
        ],
        "female_first": [
            "Maria", "Ana", "Teresa", "Helena", "Isabel", "Esperança", "Luísa", "Francisca",
            "Catarina", "Nair", "Yara", "Neide", "Katia", "Liliana", "Samira", "Edna"
        ],
        "last_names": [
            "Dos Santos", "Neto", "Fernandes", "Lopes", "Pinto", "Cardoso", "Mendes", "Tavares",
            "Cabral", "Vieira", "Semedo", "Furtado", "Moniz", "Borges", "Teixeira", "Gomes"
        ],
    },

    # 47. Armenian (Armenia)
    "armenian": {
        "male_first": ["Arman", "Davit", "Narek", "Hayk", "Gor", "Tigran", "Samvel", "Arthur", "Levon", "Karen"],
        "female_first": ["Ani", "Anahit", "Mariam", "Lilit", "Elen", "Mane", "Milena", "Nare", "Gayane", "Sona"],
        "last_names": ["Sargsyan", "Harutyunyan", "Hovhannisyan", "Hakobyan", "Grigoryan", "Petrosyan", "Gevorgyan", "Avagyan", "Ghazaryan", "Vardanyan"],
    },

    # 48. Georgian (Georgia)
    "georgian": {
        "male_first": ["Giorgi", "Davit", "Nikoloz", "Luka", "Aleksandre", "Irakli", "Zurab", "Tornike", "Levan", "Saba"],
        "female_first": ["Nino", "Mariam", "Ana", "Tamar", "Elene", "Salome", "Natia", "Khatia", "Lika", "Teona"],
        "last_names": ["Beridze", "Kapanadze", "Gelashvili", "Maisuradze", "Giorgadze", "Lomidze", "Tsiklauri", "Bolkvadze", "Nozadze", "Kvaratskhelia"],
    },

    # 49. Mongolian (Mongolia)
    "mongolian": {
        "male_first": ["Bat-Erdene", "Temüjin", "Chinggis", "Bold", "Otgonbayar", "Ganzorig", "Munkhbat", "Erdene"],
        "female_first": ["Altantsetseg", "Bayarmaa", "Enkhtuyaa", "Nomin", "Khulan", "Saruul", "Solongo", "Uranchimeg"],
        "last_names": ["Bat", "Dorj", "Boldbaatar", "Tseren", "Davaadorj", "Lkhagvasuren", "Nyamdorj", "Sukhbaatar"],
    },

    # 50. Myanmar / Burmese (Myanmar)
    "myanmar": {
        "male_first": ["Aung", "Kyaw", "Min", "Zaw", "Ko", "Thura", "Zayar", "Hein", "Myo", "Tun"],
        "female_first": ["Hnin", "Aye", "Thida", "Su", "May", "Phyu", "Khin", "Ei", "Yamin", "Nilar"],
        "last_names": ["San", "Lin", "Oo", "Win", "Naing", "Soe", "Lwin", "Htun", "Khaing", "Swe"],
    },

    # 51. Khmer (Cambodia)
    "southeast_asian_khmer": {
        "male_first": ["Sophea", "Dara", "Piseth", "Vannak", "Rithy", "Borey", "Chanthou", "Sokha"],
        "female_first": ["Kalyan", "Neary", "Bopha", "Sreymom", "Theary", "Kunthea", "Rachana", "Kolab"],
        "last_names": ["Sok", "Chan", "Chea", "Meas", "Keo", "Heng", "Kim", "Lim", "Ros", "Chhim"],
    },

    # 52. Himalayan (Bhutan)
    "himalayan": {
        "male_first": ["Tenzin", "Jigme", "Karma", "Dorji", "Sonam", "Pema", "Ugyen", "Kinley", "Sangay", "Tshering"],
        "female_first": ["Dechen", "Choden", "Wangmo", "Lhamo", "Deki", "Yeshey", "Tshering", "Karma", "Zangmo", "Tashi"],
        "last_names": ["Dorji", "Wangchuck", "Tshering", "Tobgay", "Norbu", "Gyeltshen", "Thinley", "Namgyal"],
    },

    # 53. Sahel African (Chad, Niger, Mali, Senegal)
    "sahel_african": {
        "male_first": ["Idriss", "Mahamat", "Haroun", "Abakar", "Brahim", "Issa", "Hassan", "Djibril", "Oumar"],
        "female_first": ["Fatimé", "Amina", "Mariam", "Haoua", "Zara", "Khadidja", "Achta", "Zenaba", "Fadoul"],
        "last_names": ["Deby", "Mahamat", "Abdelkerim", "Djimé", "Souleyman", "Tahir", "Kader", "Ousmane", "N'Garmbaye"],
    },

    # 54. Albanian (Albania)
    "albanian": {
        "male_first": ["Arben", "Besnik", "Dritan", "Ilir", "Kreshnik", "Luan", "Valon", "Agim", "Endrit", "Genti"],
        "female_first": ["Blerta", "Dora", "Elira", "Flutura", "Lindita", "Majlinda", "Teuta", "Vera", "Yllka", "Besa"],
        "last_names": ["Hoxha", "Shehu", "Krasniqi", "Gashi", "Berisha", "Rama", "Balla", "Mehmeti", "Kelmendi", "Morina"],
    },

    # 55. South Asian Island (Maldives)
    "south_asian_island": {
        "male_first": ["Ibrahim", "Mohamed", "Ahmed", "Ali", "Hussain", "Hassan", "Abdullah", "Ismail"],
        "female_first": ["Aishath", "Mariyam", "Fathimath", "Aminath", "Hawwa", "Zulaikha", "Shameema", "Khadeeja"],
        "last_names": ["Nasheed", "Waheed", "Solih", "Gayoom", "Zahir", "Shafeeq", "Rasheed", "Jameel"],
    },

    # 56. Turkic Caucasus (Azerbaijan)
    "turkic_caucasus": {
        "male_first": ["Ali", "Murad", "Elmir", "Tural", "Rashad", "Farid", "Eldar", "Vugar", "Kamran", "Orkhan"],
        "female_first": ["Leyla", "Aysel", "Gunel", "Nigar", "Sevda", "Sevinj", "Konul", "Samira", "Leman", "Fidan"],
        "last_names": ["Mammadov", "Aliyev", "Huseynov", "Hasanov", "Guliyev", "Ismayilov", "Ahmadov", "Abbasov", "Rzayev"],
    },

    # 57. West African Anglo (Ghana, Gambia, Liberia, Sierra Leone)
    "west_african_anglo": {
        "male_first": ["Kwame", "Kofi", "Yaw", "Kwesi", "Kojo", "Ekow", "Samuel", "Emmanuel", "David", "Michael", "Ebrima", "Lamin", "Momodou"],
        "female_first": ["Akosua", "Adwoa", "Abena", "Afia", "Yaa", "Ama", "Grace", "Mercy", "Patience", "Fatou", "Isatou", "Binta"],
        "last_names": ["Mensah", "Osei", "Boateng", "Appiah", "Agyemang", "Asante", "Owusu", "Frimpong", "Jallow", "Ceesay", "Touray", "Kamara"],
    },
}

# Fallback pool in case any unmapped code appears
DEFAULT_POOL = NAME_POOLS["anglo_western"]


def get_pool(pool_name: str) -> NamePool:
    """Retrieve pool dictionary or fallback."""
    return NAME_POOLS.get(pool_name, DEFAULT_POOL)


import random
from typing import List, Literal

GenderType = Literal["all", "male", "female"]


def generate_names(pool_name: str, count: int = 5, gender: GenderType = "all") -> List[str]:
    """
    Generate authentic cultural names from a given pool.
    - gender: 'all' (mix of male & female), 'male', or 'female'.
    - count: number of names to generate.
    Returns list of formatted strings, e.g. "👤 Shakib Hasan".
    """
    pool = get_pool(pool_name)
    males = pool["male_first"]
    females = pool["female_first"]
    surnames = pool["last_names"]

    results: List[str] = []
    for _ in range(count):
        if gender == "male":
            first = random.choice(males)
            icon = "👨"
        elif gender == "female":
            first = random.choice(females)
            icon = "👩"
        else:
            # 50/50 mix
            if random.random() < 0.5:
                first = random.choice(males)
                icon = "👨"
            else:
                first = random.choice(females)
                icon = "👩"

        last = random.choice(surnames)
        results.append(f"{icon} {first} {last}")

    return results

