# SmartNet
SmartNet Shop
Smartnet is a store that addresses the sale of equipment for Networking, which includes product purchase, shopping cart and online support.

# Data Flow Diagram
Data inside SmartNet follow the next diagram


<style>
    .mermaid svg { height: auto; }
</style>
```mermaid
graph TD
    Start[Start] --> us(User sees the catalogue of products)
    us --> cho{User choose a product?}
    cho --> |no|uc_n(User continues to view products) --> us
    cho --> |yes| uc_y(Show loggin window) --> User

    Start --> User{User is logged in?}
    Start --> |Click support| support(Show user support form) 
    support --> User
    
    User --> |no| medn(Show user 'login' and 'signup' in sidebar) --> us
    User --> |yes| medy(Show user 'My Cart' and 'Profile' in side bar)

    medy --> option{User is located in support form?}
    option --> |No| opno(User proceeds to view Catalogue and buy or add something to the cart)
    option --> |yes| opye(User proceeds to fill in the form and sending doubts) --> Start

    opno --> continue(User adds a product to the cart) 
    continue --> option2{User Click on My Cart}
    option2 --> |no| option2no(User continues in the catalogue)
    option2 --> |yes| option2yes{User proceeds to checkout?}
    option2yes --> |no| option2yno(User proceeds to view catalogue)
    option2yes --> |yes| option2yyes(User do the payment)

    
    style option2yyes fill:green
    style option2yno fill:purple
    style option2no fill:red
    style opye fill:yellow
    style medn fill:blue
    style uc_n fill:cyan
```

# Database Structure
![Database Structure](images/SmartNet_DB.png?usp=sharing)

# Main Documments about the project
- [User Manual](https://docs.google.com/document/d/1wE1DHkAu4ugy5N33-zZ9PHl6b_Hnhioj5LsaL3ywKuo/edit#heading=h.pmga95mf8jh2)
- [Technical Manual](https://docs.google.com/document/d/157dtyjpNEqb3ve3SpynsqxhJk_geGqIQRruogzvvZX0/edit?usp=sharing)
- [Data Dictionary](https://drive.google.com/file/d/1oAJAEBAfMfc9hIrT_wIkq7Z9ojCXjpAE/view)

# Project Views With Vue.js 3 Repository
- [SmartNet Linked](https://github.com/Dinotator/yorick)
# Requirements
- [Python 3.10.2](https://www.python.org/ "Python latest version")
- [FastAPI 0.75.0](https://fastapi.tiangolo.com/ "FastAPI latest version")
- [Vue.js 3 2.6.11](https://vuejs.org/ "Vue latest version")

# Installation
1. After installing python, download the current version of this repository, you can do it with the following command or download the zip archive and extract it:
``` bash
git clone https://github.com/1930346/SmartNet.git
```
2. Open a terminal and navigate to the SmartNet folder:
``` bash
cd SmartNet
```
3. Create a virtual environment and activate it:
```bash
mkdir venv
python3 -m venv venv/fastapi-mysql
```
If you are using Windows, you can use the following commands:
```pwsh
python -m venv fastapi-mysql

fastapi-mysql\Scripts\activate

```
If you are using a POSIX system (Linux, MACOS), you can use the following command:
```bash
source venv/fastapi-mysql/bin/activate
```
4. Run the following commands to install FastAPI as a package and install all the dependencies and update pip:
``` pwsh
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy pymysql cryptography databases aiomysql
```
If you are using windows:
``` pwsh
python -m pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy pymysql cryptography databases aiomysql

```
   
5. Run the following command to run the SmartNet API:
``` pwsh
uvicorn app:app --reload
```
