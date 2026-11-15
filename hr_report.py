
import csv                       
import json                       
import os                         
import sys                         
import time                        
from collections import Counter   
from datetime import datetime      
from pathlib import Path          


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "employees.csv"  
OUTPUT_DIR = BASE_DIR / "output"                
LOG_FILE = OUTPUT_DIR / "log.txt"                 




def prepare_paths():
    """1.1 ქმნის output საქაღალდეს და ამოწმებს, არის თუ არა employees.csv."""
   
    OUTPUT_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():           
        print("შეცდომა: ფაილი data/employees.csv ვერ მოიძებნა!")
        print("ჩადეთ ის 'data' საქაღალდეში და თავიდან გაუშვით.")
        return False                      

    print("ფაილის სრული მისამართი:", DATA_FILE.resolve())
    return True                          


def log(message):
    """1.3 ამატებს ერთ ხაზს log.txt-ში: დრო + შეტყობინება."""
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(datetime.now().isoformat() + " " + message + "\n")


def backup_file(src, dst):
    """1.2 აკოპირებს src ფაილს dst-ში ხაზ-ხაზ და აბრუნებს ხაზების რაოდენობას."""
    count = 0
    
    with open(src, "r", encoding="utf-8", newline="") as fin, \
            open(dst, "w", encoding="utf-8", newline="") as fout:
        for line in fin:        
            fout.write(line)   
            count = count + 1    
    return count


def do_backup():
    lines = backup_file(DATA_FILE, OUTPUT_DIR / "employees_backup.csv")
    print("გადაკოპირებული ხაზები:", lines)   


def create_lock():
    """1.4 ქმნის lock.txt-ს. თუ უკვე არსებობს, უბრალოდ გვატყობინებს."""
    try:
        
        with open(OUTPUT_DIR / "lock.txt", "x", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())
    except FileExistsError:              
        print("ანგარიში უკვე შექმნილია")  


  





def read_with_reader():
    """2.1 csv.reader - თითო ხაზს აბრუნებს როგორც სიას (list)."""
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)        
        rows = list(reader)          

    print("სათაური:", header)
    print("პირველი 3 თანამშრომელი:")
    for row in rows[:3]:            
        print("  ", row)
    print("ჩანაწერების რაოდენობა:", len(rows))


def analyze_with_dictreader():
    """2.2 csv.DictReader - თითო ხაზი არის ლექსიკონი: row["salary"]."""
    dept_count = Counter()          
    dept_salary_sum = Counter()     
    active_list = []    
    active = 0           
    inactive = 0

    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            
            salary = int(row["salary"])
            dept = row["department"]

            dept_count[dept] += 1
            dept_salary_sum[dept] += salary

            
            if row["is_active"] == "True":
                active += 1
                active_list.append((row["first_name"], row["last_name"], salary))
            else:
                inactive += 1

   
    stats = []
    for dept in dept_count:
        avg = round(dept_salary_sum[dept] / dept_count[dept], 2)
        stats.append({
            "department": dept,
            "employee_count": dept_count[dept],
            "avg_salary": avg,
        })
        stats.sort(key=lambda s: s["avg_salary"], reverse=True)

    print("\nთანამშრომლები დეპარტამენტებში:")
    for s in stats:
        print("  ", s["department"], s["employee_count"])

    print("\nსაშუალო ხელფასი დეპარტამენტებში:")
    for s in stats:
        print("  ", s["department"], f"{s['avg_salary']:.2f}")


    top3 = sorted(active_list, key=lambda e: e[2], reverse=True)[:3]
    print("\nTOP 3 აქტიური თანამშრომელი:")
    for first, last, salary in top3:
        print("  ", first, last, salary)

    print("\nაქტიური:", active, "| არააქტიური:", inactive)
    return stats      


def write_department_stats(stats):
    """2.3 csv.DictWriter - ვწერთ ლექსიკონებს CSV-ში."""
    path = OUTPUT_DIR / "department_stats.csv"
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["department", "employee_count", "avg_salary"])
        writer.writeheader()       
        writer.writerows(stats)     
    print("ჩაიწერა:", path.name)


def write_high_earners():
    """2.4 csv.writer - ვწერთ აქტიურებს, რომელთა ხელფასი >= 5000."""
    rows = []
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["is_active"] == "True" and int(row["salary"]) >= 5000:
                full_name = row["first_name"] + " " + row["last_name"]
                rows.append([row["id"], full_name, row["department"],
                             int(row["salary"])])

    path = OUTPUT_DIR / "high_earners.csv"
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "full_name", "department", "salary"])  
        writer.writerows(rows)                                       
    print(path.name, "- ჩანაწერები:", len(rows))   















def safe_read(path):
    """3.1 ფაილის წაკითხვა ისე, რომ პროგრამა შეცდომაზე არ გაჩერდეს."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        
        log("ფაილი ვერ მოიძებნა: " + str(path))
        return ""
    except UnicodeDecodeError:
        
        log("წაკითხვის (დეკოდირების) შეცდომა: " + str(path))
        
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()


def test_safe_read():
    missing = OUTPUT_DIR / "missing.txt"    
    broken = OUTPUT_DIR / "broken.txt"      

  
    with open(broken, "wb") as f:
        f.write(bytes([99, 97, 102, 233, 32, 255]))

    print("missing.txt ->", repr(safe_read(missing)))
    print("broken.txt  ->", repr(safe_read(broken)))


def count_cities():
    """3.2 Counter - ითვლის, რამდენჯერ გვხვდება თითო ქალაქი."""
    cities = Counter()
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            cities[row["city"]] += 1

    top3 = cities.most_common(3)    

    print("\nქალაქების TOP 3:")
    for city, n in top3:
        print("  ", city, n)

   
    with open(OUTPUT_DIR / "cities.txt", "w", encoding="utf-8") as f:
        for city, n in top3:
            print(city, n, file=f)


def save_json_safe(data, path):
    """3.3 უსაფრთხო შენახვა: ჯერ დროებით ფაილში, მერე ჩანაცვლება.
    თუ შუაში პროგრამა გაჩერდა, ძველი ფაილი დაუზიანებელი რჩება."""
    tmp_path = str(path) + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, path)      











class Timer:
    """გამოყენება:  with Timer("სახელი"):  ...კოდი...
    ბეჭდავს START და FINISH და ზომავს, რამდენი ხანი გაგრძელდა."""

    def __init__(self, name):
        self.name = name
        self.start = None

    def __enter__(self):
        
        print("START", self.name)
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        
        elapsed = time.perf_counter() - self.start
        if exc_type is not None:    
            print("FAILED " + self.name + ": " + exc_type.__name__)
            return False             
        print("FINISH", self.name, f"({elapsed:.4f} წმ)")
        return False


def timer_demo():
    """4.2 განზრახ ვაკეთებთ შეცდომას (1/0) და with-ს გარეთ ვიჭერთ."""
    try:
        with Timer("test"):
            1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError დავიჭირეთ with-ის გარეთ")




def main():
    if not prepare_paths():          
        sys.exit(1)                  

    log("პროგრამა დაიწყო")

    do_backup()
    log("ასლი შეიქმნა")

    create_lock()
    log("lock დამუშავდა")

    
    with Timer("CSV ანალიზი"):
        read_with_reader()
        stats = analyze_with_dictreader()
        write_department_stats(stats)
        write_high_earners()
    log("ნაწილი 2 დასრულდა")

    test_safe_read()
    count_cities()
    save_json_safe(stats, OUTPUT_DIR / "summary.json")
    log("ნაწილი 3 დასრულდა")

    timer_demo()
    log("პროგრამა დასრულდა")



if __name__ == "__main__":
    main()










# 1. რატომ არის "w" სახიფათო?
#    "w" რეჟიმი ფაილს გახსნისთანავე ცარიელს ხდის. თუ ფაილში რამე იყო,
#    ის სამუდამოდ წაიშლება. არსებული ფაილის დასაცავად გამოვიყენებდი "a"-ს
#    (ბოლოში ამატებს, არაფერს შლის). თუ მინდა, რომ ახალი ფაილი შეიქმნას
#    და არსებული არასდროს გადაიწეროს, გამოვიყენებდი "x"-ს.
#
# 2. რას აკეთებს __exit__() და რატომ ჯობია with ხელით close()-ს?
#    __exit__() ავტომატურად ეშვება with ბლოკის დასრულებისას და ფაილს
#    ხურავს. ეს ხდება მაშინაც, როცა ბლოკში შეცდომა მოხდება. ხელით close()-ს
#    შეიძლება დავივიწყოთ, ან შეცდომის გამო ის საერთოდ ვერ შესრულდეს და
#    ფაილი ღია დარჩეს.
#
# 3. რატომ არ უნდა დავამუშაოთ CSV split(',')-ით?
#    ზოგჯერ მძიმე თვითონ მონაცემის შიგნითაა, ბრჭყალებში. მაგალითად, ხაზი
#    1,"Tbilisi, Georgia",5000 უნდა იყოს 3 ველი, მაგრამ split(',') მას
#    4 ნაწილად დაჭრის და სვეტები აირევა. csv მოდული ბრჭყალებს სწორად
#    აღიქვამს და 3 ველს დააბრუნებს.




























