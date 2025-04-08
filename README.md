# 🔐 PassSentinel

**PassSentinel** is a cybersecurity-focused password auditing tool that ensures strong password hygiene by using regex and entropy calculations. It checks for password leaks using the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API with k-anonymity for private data checking and securely manages verified password hashes in a local SQLite database.

---

## ⚙️  Cybersecurity Relevance

PassSentinel simulates a **real-world security auditing pipeline** by:

- Enforcing **strong password practices** with regex + entropy validation
- Checking for exposure in known **data breaches**
- Tracking **leak status over time**
- Automating **daily scanning tasks**
- Promoting awareness of **vulnerability detection workflows**

---

## 🚦 Program Flow

### 🧩 Step 1: Password Strength Validation (`./run.sh`)
User is prompted to enter a password.

#### ✅ Validation criteria:
- **Length:** ≥ 12 characters
- **Uppercase:** at least one `[A-Z]`
- **Lowercase:** at least one `[a-z]`
- **Digits:** at least two `[0-9]`
- **Special Characters:** at least one `[!@#$%^&*(),.?":{}|<>]`

Regex is used to check each condition and identify what's missing.

#### 🔐 Entropy-based Strength Meter:

| Entropy Score | Classification   |
|---------------|------------------|
| > 80          | Very Strong ✅    |
| > 60          | Strong ✅         |
| > 40          | Moderate ⚠️      |
| ≤ 40          | Weak ⚠️          |

> Users must reenter their password if it is Weak or Moderate. They are shown suggestions for improvement based on what criteria they failed.

---

### 🧪 Step 2: Leak Verification via HIBP API

Once the password is **Strong** or **Very Strong**, the user reenters it to check for **known leaks** using the Have I Been Pwned API.  
- If found in a breach ➜ user is asked to choose another password.
- If not found ➜ the password is **SHA-1 hashed** and stored in the local SQLite database.

---

### 🧬 Step 3: Leak Scan for All Stored Passwords (`./rds.sh`)

- All hashes in the database are scanned using the HIBP API.
- If a password is found to be leaked:
  - `confirmed_leaks` counter is incremented by 1
  - Status is updated to **LEAKED ⚠️**
- If not leaked:
  - Status remains **SAFE ✅**

A table with all records can be viewed using the built-in viewer.

---

### ⏰ Step 4: Daily Leak Scan Automation

The database scan is scheduled to **automatically run daily at 09:00** using Python’s `schedule` module.

```python
import time
import schedule

# Automation. passwords in databse must be verified for leaks every day at 09:00
def job(): 

    verify_all_hashes(limit=100) 
    view_table() 

schedule.every().day.at("09:00").do(job)

while True: 
    schedule.run_pending()
    time.sleep(60)
```
---

## 📊 Database Table Structure

| column        | type          |Description  |
|---------------|---------------|-------------|
|  hash         |  TEXT         | 	SHA-1 hashed password             |
| confirmed_leaks|  INTEGER     |  Counter of confirmed leaks          |
| status        |  TEXT         |  LEAKED ⚠️ or SAFE ✅             |

---

## 🧠 Skills Acquired – Cybersecurity Focus

By building PassSentinel, I deepened my knowledge in:

- ✅ Regex validation for secure password enforcement
- ✅ Entropy-based strength classification
- ✅ Secure hashing algorithms (SHA-1)
- ✅ API integration with k-anonymity for private data checking
- ✅ Database handling of security-sensitive information
- ✅ Task scheduling for continuous monitoring

---

## 🖥 Example CLI Session

```bash
$ ./run.sh
Enter your password:
> hunter123

Password Strength: Moderate ⚠️
Entropy: 46.53 bits
Password is not strong enough, please read these recommendations and try again
Recommendations 💡:
- Use at least 12 characters in the password
- Add atleast one uppercase letter in the password
- Use special characters in the password
...
 Enter a password:
> Hunter11155555###$$$

Password Strength: Very Strong✅
Entropy: 131.09 bits

Enter your password again, to check for a possible leak:
> Hunter11155555###$$$

Your password has not been found in any breaches and has now been added to the database ✅
```
---

```bash
$ ./rds.sh
Checking for leaks...⏳
    hash                                       confirmed_leaks  status
0   CBFDAC6008F9CAB4083784CBD1874F76618D2A97                6   LEAKED ⚠️
1   D033E22AE348AEB5660FC2140AEC35850C4DA997                6   LEAKED ⚠️
2   4E30F0F8E71F6A20F48D0AEA6087FC64CFE3E262                0     SAFE ✅
3   A8A00ADEBF1411B8BAF07BDC688CE3889E8F7CB2                6   LEAKED ⚠️
4   9BC34549D565D9505B287DE0CD20AC77BE1D3F2C                6   LEAKED ⚠️
5   54B869057F5253A9C3B201428BEFE69D050E65CD                6   LEAKED ⚠️
6   014DCCEB922DEF2523B998CC98049DB3817D8D69                6   LEAKED ⚠️
7   6DB65D1CB30D833AD80BD01AA0F09B6FF77ED4E8                0     SAFE ✅
8   D12759744941336D3EFD6577AD1CD3A86332A72E                0     SAFE ✅
9   0EC51B3D23F552BFB0ABE925B1A1EB01A16C9501                6   LEAKED ⚠️
10  EB87A50D1D861815EE9D1219EAD41A562F6A5DF9                0     SAFE ✅
11  99CE9AF7F63EDA8463A1DCBA8C3047525ECFF954                0     SAFE ✅
12  60D8CDF7FB3F502C0911F15591A1C7A287C36361                0     SAFE ✅

Passwords are automatically checked for possible leaks everyday at 09:00 ⏳
```
> Password entered by user is #12 on the database in sha1 format (Hunter11155555###$$$)

---  

## 🛠 Getting Started

1. Clone the repo:
   ```bash
    git clone https://github.com/TGrandeZA/PassSentinel.git
    cd PassSentinel
2. Install dependencies
   ```bash
    pip install -r requirements.txt

3. run password check
   ```bash
    ./run.sh

4. run database scan
   ```bash
    ./rds.sh
   ```






