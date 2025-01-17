# Order & Load Business Intelligence v1

This document presents the Order & Load BI Software in 4 main chapters under the headings of Introduction, Desktop User Application, Server Application and Data Modeling. It aims to enrich the content with Gifs and Screenshots.

In order to make sense of the codes, it is important to have basic knowledge of **Python**, **pymongo** and **pyqt5**.

This project aims to contribute to the fields of **user interface, artificial intelligence, data collection, data analysis, data management and digitization of business processes**, rather than making commercial gains.

**Note** : Instead of saying "it could have been better this way or that way" many times in the document, I would like to state that I did not prepare much for the project in advance,
it grew on its own as I added new features and I did it to enjoy it. Therefore, in order to see the result,
I skipped some requirements when you take a look at the codes.
However, I would like to underline that it has features that can answer the questions of many developers I encountered during my research.
When I started the project, I was new to the libraries I used, but with my current knowledge, I believe that I can finish this project in half time, which I finished in 3 weeks.

Navigate Through Chapters,
- [Introduction](#introduction)
  - [Functions](#functions)
  - [FAQ](#faq)
- [User Interface](#user-interface)
  - [Splash & Login](#splash--login) 
  - [Settings Forms](#settings-forms)
  - [Order Form](#order-form)
  - [Main Window](#main-window)
  - [Report Form](#report-form)
- [Server Application](#server-application)
  - [Timer](#timer) 
  - [Filter](#filter) 
  - [Recorder](#recorder) 
  - [Notifier](#recorder) 
- [Data Modelling](#data-modelling)
  - [Customers](#customers) 
  - [Cargos](#cargos)
  - [Products](#products)
  - [Orders](#orders)
  - [Notifications](#notifications)
  - [Server Log](#server-log)
- [How to Convert a Project to App?](#how-to-convert-a-project-to-app-)
- [How to Contribute?](#how-to-contribute-)

  
## Introduction

It enables to make processes safer and faster in terms of operation and follow-up until the added orders are shipped.
Thanks to its easy use, it aims to save time for the departments. In short, it contributes to the transformation of raw data into a meaningful business process. This proccesses designed to serve to a Textile Company. Please consider that products are kept as fabric roll of approximately 50 Meter in stock, then these are cutted according to customers's orders such as only 5 Meter. 

On the **Artificial Intelligence** side of the project, enhanced thinking and data analysis capability was emphasized during the design of the processes. <br>
**Search Algorithm**, which enables the user to avoid mistakes and take faster action during the product selection phase,<br>
**Root Finding Algorithms** that check whether the inputs received from the user are of Integer or Float data type,<br>
**Sorting Algorithm** that offers dynamic use of filtering and display settings while browsing reports,<br>
**Genetic Algorithms**, which provide only relevant data by e-mail in formats that change from event to event, at the stages where follow-up is very important,
as a addition, **functions that only work on** the server side at **certain times** and **conditions** show that this program makes serious use of artificial intelligence.

On the **User Interface** side, the principle of simplicity has been acted upon and it is aimed to perform all operations with the keyboard as much as possible.
The classes of windows are imported into the main file(**main.py**), and objects are derived from these classes in the App class.
Most of functions except closeEvent functions are defined in the main file so that they can be observed together.
Only the functions of the splash and report classes are defined in the source file from which they are imported.
This build was not intentionally created, but gave the developers a chance to experiment with two different methods. <br>
Please be aware that aesthetic concerns have been ignored.

One of the most important points in applications like this is the correct **Data Modelling**. 
Applications that are successful in this regard are likely to produce more practical solutions on the user interface and backend.
As a result, it is necessary to prepare environments where faster and less error-prone queries can be made for successful analysis and management of data.

Except for internet outages, most possible **Error** situations have been brought under control.
In any case, if there is no disconnection during the query phases, data corruption will not occur.

### Functions
Below is a general summary of the program's functions.
-	Adding, Editing and Deleting Customer and Cargo Informations.
-	Automatic Assignment and Sorting of Order Code
-	Adding an Order
-	Automatic Transmission of the details of the added order to the relevant customer and operation team in e-mail format
-	Thanks to the well-designed MongoDB Database Model, Tracking and Management of the order on a product basis, even if it is entered in bulk
-	Instant Tracking of All Orders from the Main Screen
-	Adding Note to an order after adding
-	Splitting Orders
-	Managing Orders (Cancellation, Preparation, Holding, Completion and Loading)
-	In case the order cannot be supplied, Adding a Reason for Waiting to the Holding Order
-	Automatic Transmission of the Holding Order to the supply unit in e-mail format along with the reason for the waiting
-	Adding an Information Note to the Holding Order about when or how it will be supplied
-	Detailed Reporting of Orders
-	Customized Settings in Order Reports (Filtering, Display Settings)
-	Converting Order Reports as an Excel File
-	Server Application Automatically Forwarding the loading details made during the day to the relevant customers at the end of the day in e-mail format
-	Automatically Transmitting Shutdown or Error situations that may occur in the Server Application to the technical unit in an instant mail format

### FAQ
Below you can see some of the frequently asked questions by the developers in several platform, which you can find answers to or get ideas from in this project.
#### PyQt5
-	How to make a multi-window application with PyQt5?
-	What kind of errors need to be avoided when developing a multi-window application with PyQt5?
-	How to assign signal-slots in PyQt5?
-	How to dynamically pass data to QTableWidget?
-	How to add close event in widgets?
-	How to create shortcut object with QShorcut on windows?
-	How can I access the information in the selected row on the QTableWidget?
-	How can I get a new row to be added when it comes to the last row in QTableWidget?
#### MongoDB
-	How should user name and password control be provided via MongoDB?
-	How to access, filter and sort fields in nested dictionary data type?
-	How to add new values, update and delete fields in nested dictionary data type?
-	How to add new keys and values to arrays?
-	How can arrays be updated?
-	How to associate documents in different collections?
#### Others
-	How to send mail with Python?
-	How to control keyboard keys with Python?
-	How to manage settings locally with json file?
-	How to read file and apply data with Pandas library?
-	How to synchronize data and export to excel file with Openpyexcel library?

## User Interface

In this chapter, the windows that represent the front-end of the application, the structure that makes it functional, and the database management will also be mentioned. 
This UI is designed in Turkish to be able to be tested by users.

### Splash & Login
It would be more appropriate to evaluate the Splash and Login screens together because users cannot intervene until the login screen is opened.

![splash-login](https://user-images.githubusercontent.com/69144354/149879188-f9296f40-b7d1-43ca-be83-8ed56147ce7f.gif)

#### Splash 
The Splash Screen has been added to the program symbolically. It is aimed to give an idea about how creative work can be done on the frontend with the **PyQt5** library.
##### Progress Bar Animation
```python
class  SplashScreen(QtWidgets.QMainWindow):
  def __init__(self):
      super(SplashScreen,self).__init__()

      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.additional_UiSetup()

      self.ui.label_softwareName.setText("ORDER & LOAD BUSINESS INTELLIGENCE SOFTWARE v1")
      
      # Starting Value of the Progress Bar
      self.counter = 0

      # Timer 
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.progress) # That is a signal which detect the timeout to call the function of the "progress"
      self.timer.start(35)

  def progress(self):
  # Setting Starting Value of the Splash Screen
  self.ui.progressBar.setValue(self.counter)
  
  # To rise the Value of the Progress Bar
  self.counter += 1 

  if self.counter > 70:
      self.ui.lbl_loading.setText("configurations setting...")

  if self.counter > 80:
      self.ui.lbl_loading.setText("data proccessing...")

  if self.counter > 95:
      self.ui.lbl_loading.setText("app started.")

  if self.counter > 100:
      self.ui.check_close.setChecked(True)
      self.timer.stop()
      self.close()
 ```
##### Frameless Design
```python
def additional_UiSetup(self):
  # To set the Widget Frameless
  flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
  self.setWindowFlags(flags)

  # To remove the background of the Widget
  self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

  # To set Shadow Effect on the Widget
  self.shadow = QGraphicsDropShadowEffect(self)
  self.shadow.setBlurRadius(20)
  self.shadow.setXOffset(0)
  self.shadow.setYOffset(0)
  self.shadow.setColor(QtGui.QColor(0,0,0,60))
  self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
```
#### Login
It is important to mention two important functions in this section. One of them is Username and Password control and the other is the storage of these information.
##### Control Mechanism
Verifying user information is the most important part of applications in terms of security. As a method, it may be possible to read the scripts of some encrypted files from an online repo. However, it would be more practical and secure for an application of this scale to have MongoDB do this control phase.

To summarize, every time the login button is pressed, it places the username and password information in the MongoDB **Connection String** and sends a query. If an **Authorization Error** is returned, it indicates incorrect information.

```python
def check_user(self):
        print("User informations is checked.")
        username_entry = self.login.ui.txt_username.text() 
        password_entry = self.login.ui.txt_password.text()

    #   To use this method, users must be already created at database 
    #   Thanks to that, mongodb database check if username and password is valid or not by itself.
    try:                         
        self.myclient = pymongo.MongoClient(f"mongodb+srv://{username_entry}:{password_entry}@cluster0.asdnj.mongodb.net/app_test?retryWrites=true&w=majority")
        self.mydb = self.myclient["order-load"]
        self.customer_coll = self.mydb["customers"]
        self.cargo_coll = self.mydb["cargos"]
        self.order_coll = self.mydb["orders"]
        self.product_coll = self.mydb["products"]
        self.setting_coll = self.mydb["settings"]
        result = self.customer_coll.find_one() #  This one is used to send a request to database to be sure if user is valid or not.

        self.username = self.login.ui.txt_username.text() 
        self.password = self.login.ui.txt_password.text()

        print(f"User '{self.username}' in online.")
        self.login.close()
        self.load_data_to_windows()

        if self.login.ui.checkBox.isChecked() == True:
            with open("settings.json","r",encoding="utf-8") as file:
                settings = json.load(file) 
            settings["remember_me"]["isChecked"] = True
            settings["remember_me"]["username"] = self.username
            settings["remember_me"]["password"] = self.password
            with open("settings.json","w",encoding="utf-8") as file:
                json.dump(settings, file)
        else:
            with open("settings.json","r",encoding="utf-8") as file:
                settings = json.load(file) 
            settings["remember_me"]["isChecked"] = False
            settings["remember_me"]["username"] = ""
            settings["remember_me"]["password"] = ""
            with open("settings.json","w",encoding="utf-8") as file:
                json.dump(settings, file)

        self.window.ui.lbl_user.setText(self.username)
        self.window.show()

    #   If Username or password is not valid mongodb throws a Authorizaiton error
    #   When program catch this error, that means username or password is not valid. 
    except pymongo.errors.OperationFailure and pymongo.errors.InvalidURI and pymongo.errors.OperationFailure:
        self.login.hide()
        msg = QMessageBox()
        msg.setWindowTitle("Geçersiz İşlem")
        msg.setText("Kullanıcı Adı veya Parola yanlış!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.activateWindow()
        msg.raise_()
        x = msg.exec_()
        self.login.show()
```
##### Storage of Username and Password
In order to store this information, there is a json type document waiting locally.
###### settings.json
```json
{
  "remember_me": {
  "isChecked": true,
  "username": "cuneyttopbas",
  "password": "cuneyttopbas123"
  }
}
```
The codes below are read without opening the login screen. The structure constructed here is based on reading the **settings.json** page first. If the value of the **"isChecked"** key is **"true"**, it transfers the user information from the same file directly to the login screen.
```python
if self.login.ui.checkBox.isChecked() == True:
    with open("settings.json","r",encoding="utf-8") as file:
        settings = json.load(file) 
    settings["remember_me"]["isChecked"] = True
    settings["remember_me"]["username"] = self.username
    settings["remember_me"]["password"] = self.password
    with open("settings.json","w",encoding="utf-8") as file:
        json.dump(settings, file)
else:
    with open("settings.json","r",encoding="utf-8") as file:
        settings = json.load(file) 
    settings["remember_me"]["isChecked"] = False
    settings["remember_me"]["username"] = ""
    settings["remember_me"]["password"] = ""
    with open("settings.json","w",encoding="utf-8") as file:
        json.dump(settings, file)
```
### Settings Forms
Assuming there is no data in the database yet except products, customer and shipping information must be added first to take advantage of the program's functions.

![settings](https://user-images.githubusercontent.com/69144354/149901521-f0b5e4f3-03a5-47e1-a1dc-9159cc0f2404.gif)

In order to create the structure above, some important steps are shared below.
#### Management of the Data
##### Add a Customer
###### Step 1
A Stacked Widget is set to organize Customers and Cargos Menus at the same widget so if a user information is going to be added, then we need to set a current index detail for the stacked widget.
```python
def open_customer_settings_to_add(self):
    self.setting_form.ui.stackedWidget.setCurrentIndex(0)
    self.setting_form.show()
```

###### Step 2
Signal-Slot to detect a press on the **Save** Button
```python
self.setting_form.ui.btn_save_customer.clicked.connect(self.add_customer)
```
Function
```python
def add_customer(self):
  try:
    if self.setting_form.ui.txt_company is not None:  # It must be sure that at least Company name is entered to make a query
        print("not none olduğu tespit edildi")
        company = self.setting_form.ui.txt_company.text()
        mail1 = self.setting_form.ui.txt_mail1.text()
        mail2 = self.setting_form.ui.txt_mail2.text()
        mail3 = self.setting_form.ui.txt_mail3.text()
        extra_code = self.setting_form.ui.cb_extra_code.isChecked()
        notification = self.setting_form.ui.cb_notification.isChecked()

        self.customer_data = {
            "_id"  :company,
            "mail1" :mail1,
            "mail2" :mail2,
            "mail3" :mail3,
            "extra_code":extra_code,
            "notification":notification
        } 
        self.customer_coll.insert_one(self.customer_data)
        self.feedback_messageBox(company,"eklendi")
        self.setting_form.close()
        self.clear_customer_settings()

  except pymongo.errors.DuplicateKeyError: # This Exception is used when editing the customer document. 
    self.customer_coll.update_one(
        {"_id" : company,},
        {"$set": {
         "mail1":mail1,
         "mail2":mail2,
         "mail3":mail3,
         "extra_code":extra_code,
         "notification":notification
        }}
    )
    self.feedback_messageBox(company,"düzenlendi")
    self.setting_form.close()
    self.clear_customer_settings()
  self.refresh_setting()
```
##### Edit a Customer
###### Step 1
```python
def open_customer_settings_to_edit(self):
        item = self.select_clicked_item(self.settings.ui.customer_listWidget)
        customer = self.customer_coll.find_one({"_id":item.text()})
        
        # Details of the Customer is coming from the Database via "_id" info that we can access from List Widget
        self.setting_form.ui.txt_company.setText(item.text())     
        self.setting_form.ui.txt_company.setEnabled(False)
        self.setting_form.ui.txt_mail1.setText(customer["mail1"]) 
        self.setting_form.ui.txt_mail2.setText(customer["mail2"])
        self.setting_form.ui.txt_mail3.setText(customer["mail3"])
        self.setting_form.ui.cb_extra_code.setChecked(customer["extra_code"])
        self.setting_form.ui.cb_notification.setChecked(customer["notification"])

        self.setting_form.ui.stackedWidget.setCurrentIndex(0)
        self.setting_form.show()
```
Cick on this link to see how to select a item of QListWidget, [Selecting Items of QListWidget](#selecting-items-of-qlistwidget)
###### Step 2
As you can see below, same fuction which is used adding is used here as well, thanks to Exception function can detect if it is a adding or editing. If MongoDb throws a **"Duplicate"** error that means there is one more with the same "_id" so this is a editing.

Signal-Slot to detect a press on the **Save** Button
```python
self.setting_form.ui.btn_save_customer.clicked.connect(self.add_customer)
```
Function
```python
def add_customer(self):
  try:
    if self.setting_form.ui.txt_company is not None:  # It must be sure that at least Company name is entered to make a query
        print("not none olduğu tespit edildi")
        company = self.setting_form.ui.txt_company.text()
        mail1 = self.setting_form.ui.txt_mail1.text()
        mail2 = self.setting_form.ui.txt_mail2.text()
        mail3 = self.setting_form.ui.txt_mail3.text()
        extra_code = self.setting_form.ui.cb_extra_code.isChecked()
        notification = self.setting_form.ui.cb_notification.isChecked()

        self.customer_data = {
            "_id"  :company,
            "mail1" :mail1,
            "mail2" :mail2,
            "mail3" :mail3,
            "extra_code":extra_code,
            "notification":notification
        } 
        self.customer_coll.insert_one(self.customer_data)
        self.feedback_messageBox(company,"eklendi")
        self.setting_form.close()
        self.clear_customer_settings()

  except pymongo.errors.DuplicateKeyError: # This Exception is used when editing the customer document. 
    self.customer_coll.update_one(
        {"_id" : company,},
        {"$set": {
         "mail1":mail1,
         "mail2":mail2,
         "mail3":mail3,
         "extra_code":extra_code,
         "notification":notification
        }}
    )
    self.feedback_messageBox(company,"düzenlendi")
    self.setting_form.close()
    self.clear_customer_settings()
  self.refresh_setting()
```
##### Remove a Customer
```python
item = self.select_clicked_item(self.settings.ui.customer_listWidget)
if item is not None:
    self.customer_coll.delete_one({"_id":item.text()})
    self.feedback_messageBox(item.text(),"silindi")
    self.refresh_setting()
```

#### Selecting Items of QListWidget
```python
def select_clicked_item(self,listWidget):
    index = listWidget.currentRow()
    item = listWidget.item(index)

    return item
```
#### Display Settings of QListWidget
```python 
def load_settings_data(self):
    for customer in self.customer_coll.find():
        customer_name = customer["_id"]
        self.settings.ui.customer_listWidget.addItem(customer_name)

    for cargo in self.cargo_coll.find():
        cargo_name = cargo["_id"]
        self.settings.ui.cargo_listWidget.addItem(cargo_name)
```
### Order Form
An order can be added as it has Customer and Cargo information as well. The Order Form was created to add an order. Some partial edits can be performed from the [Main Window](#main-window).

![order](https://user-images.githubusercontent.com/69144354/149923071-f4e49d7c-0e83-435d-85e7-eaf0905e052d.gif)
#### Searching Products or Variant Codes
In cases where the number of products and their variants is high, the best way to perform fast and error-free transactions is to create a good search mechanism.
##### Shortcut to Access Searching Form
From imported class named OrderWindow(), a "self.order" object is created.
Documents which is imported in the codes below can be seen in source files.
```python
from orderForm.order import OrderWindow 
self.order = OrderWindow()
```
Object of QShortcut is created as a child of Order Form class 
```python
self.shortcut_open1 = QShortcut(QKeySequence('F1'), self.order)
self.shortcut_open1.activated.connect(self.open_searchingForm)
```
###### Function
```python
def open_searchingForm(self):
  try:
      if self.selected_column == 0: # If selected Column is "0", that means the user is looking for a product
          text = self.order.ui.table_details.item(self.selected_row, self.selected_column)
          if text is not None:
              print(text.text())
              self.searching_form.ui.txt_search.setText(text.text())
              for product in self.product_coll.find({"_id":{"$regex": f"^{text.text().upper()}"}}):
                  product_name = product["_id"]
                  self.searching_form.ui.searching_list.addItem(str(product_name))
              self.searching_form.show()
          else:
              self.searching_form.ui.txt_search.setText("")
              for product in self.product_coll.find().sort("_id",1):
                  product_name = product["_id"]
                  self.searching_form.ui.searching_list.addItem(str(product_name))
              self.searching_form.show()

      elif self.selected_column == 1: #If selected Column is "1", it assumes that the user is looking for color codes of a product already choosen
          text = self.order.ui.table_details.item(self.selected_row, self.selected_column)
          if text is not None:
              self.searching_form.ui.txt_search.setText(text.text())
              product_name = self.order.ui.table_details.item(self.selected_row, 0)
              if product_name is not None: # It check if product is choosen or not
                  for product in self.product_coll.find({"_id": product_name.text().upper}):
                      lenght = len(product["color_codes"])
                      for i in range(lenght):
                          if text.text() in product["color_codes"][i][-2:]:
                              self.searching_form.ui.searching_list.addItem(product["color_codes"][i])
                  self.searching_form.show()
              else:
                  self.warning_messageBox("Ürün seçimi yapılmadı!")

          else:
              product_name = self.order.ui.table_details.item(self.selected_row, 0)
              if product_name is not None:
                  for product in self.product_coll.find({"_id": product_name.text().upper()}):
                      lenght = len(product["color_codes"])
                      for i in range(lenght):
                          self.searching_form.ui.searching_list.addItem(product["color_codes"][i])
                  self.searching_form.show()
              else:
                  self.warning_messageBox("Ürün seçimi yapılmadı!")

  except AttributeError:
      print("F1 Kynaklı attribute error çalıştı")
      self.set_focus()
  except  pymongo.errors.PyMongoError:
      self.warning_messageBox("İnternet bağlantınızı kontrol ediniz!")
      self.order.close()
```

#### UI of the Form
Important interface features such as loading of customer and cargo details in the combobox of Order Form and, if selected, accompanying their information and adding a new line automatically as the line progresses, are mentioned below.

##### Loading Necessary Datas to Form
###### Step 1
```python
self.order.ui.cb_cargos.clear()
self.order.ui.cb_customers.clear()

# If any item is selected 
# To load Customer Combobox with customer infos
self.order.ui.cb_customers.addItem(" ")
for customer in self.customer_coll.find():
    customer_name = customer["_id"]
    self.order.ui.cb_customers.addItem(customer_name)

# To load Cargo Combobox with cargo infos
self.order.ui.cb_cargos.addItem(" ")
for cargo in self.cargo_coll.find():
    cargo_name = cargo["_id"]
    self.order.ui.cb_cargos.addItem(cargo_name)  
    
    
today = date.today()
year = today.year
month = today.month
day = today.day

self.order.ui.order_date.setDate(QtCore.QDate(year, month, day)) # Load the current date to QtDate 

self.order.ui.table_details.selectionModel().selectionChanged.connect(self.on_selectionChanged) # When user tabs to last cell, one more row is crated by itself
self.order.ui.cb_cargos.currentTextChanged.connect(self.transfer_info_on_form)                  # Transfer selected customer's info to relevant QtLineEdits
self.order.ui.cb_customers.currentTextChanged.connect(self.transfer_info_on_form)               # Transfer selected cargo's info to relevant QtLineEdits
```
###### Step 2
This function is called only if item of combobox of customer or cargo is changed, change actually means user choosed a one
```python
def transfer_info_on_form(self):
  try:
      if self.cargo_coll.find_one({"_id":self.order.ui.cb_cargos.currentText()}) is not None:
          cargo = self.cargo_coll.find_one({"_id":self.order.ui.cb_cargos.currentText()})
          if self.order.ui.cb_cargos is not None:
              self.order.ui.txt_ship_adress.setText(cargo["adress"])
              self.order.ui.txt_ship_tel.setText(cargo["phone"])
      else:
          self.order.ui.txt_ship_adress.clear()
          self.order.ui.txt_ship_tel.clear()              

      if self.customer_coll.find_one({"_id":self.order.ui.cb_customers.currentText()}) is not None:
          customer = self.customer_coll.find_one({"_id":self.order.ui.cb_customers.currentText()})
          if self.order.ui.cb_cargos is not None:
              self.order.ui.txt_receiver_name.setText(customer["_id"])
      else:
          self.order.ui.txt_receiver_name.setText("")

  except  pymongo.errors.PyMongoError:
      self.warning_messageBox("İnternet bağlantınızı kontrol ediniz!")
      self.order.close()
```
##### Automatic Row Adding to QTableWidget
###### Step 1
That line of code is written to detect ant change of selection on the QTableWidget
```python
self.order.ui.table_details.selectionModel().selectionChanged.connect(self.on_selectionChanged)
```
###### Step 2
After detecting change on the QTableWidget, function below is check if selected row and column are the last ones. If it is True, then add a new row.
```python
def on_selectionChanged(self,selected):
    for ix in selected.indexes():
        print(f"Selected Cell Location Row {ix.row()} , Column {ix.column()}")
        self.selected_column = ix.column()
        print(f"selected column {self.selected_column}")
        self.selected_row = ix.row()
        print(f"selected row {self.selected_row}")
        rowCount = self.order.ui.table_details.rowCount()
        columnCount = self.order.ui.table_details.columnCount()
        if ix.row() == (rowCount-1) and ix.column() == (columnCount-1):
            self.order.ui.table_details.insertRow(rowCount)
```
#### Adding Order
When adding an order, it is sufficient to enter the company name and at least one product with all its information. As it is a sensitive stage as well as important,that is why management of errors is also a imperative.

```python
def save_order(self):
    try:
        
        company = self.order.ui.cb_customers.currentText()
        # Receiver Details
        receiver = self.order.ui.txt_receiver_name.text()
        authority = self.order.ui.txt_author.text()
        company_phone = self.order.ui.txt_cust_tel.text()
        company_gsm = self.order.ui.txt_gsm_tel.text()
        company_adress = self.order.ui.txt_cust_adress.text()

        # Shipment Details 
        shipper_name = self.order.ui.cb_cargos.currentText()
        customer_code = self.order.ui.txt_customer_code.text()
        ship_type = self.order.ui.txt_ship_type.text()
        ship_phone = self.order.ui.txt_ship_tel.text()
        ship_adress = self.order.ui.txt_ship_adress.text()

        # Order Date
        order_date = self.order.ui.order_date.text()

        # Order Creation Date
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # To create a specific code for each order
        order_code = self.create_orderCode(company)

        # Transferring datas to a dictionary to send database together
        self.order_data = {
            "_id": order_code,
            "Company Name" : company,
            "Crated_by":self.username,
            "Created_at": created_at,
            "Order_at" : order_date,
            "Receiver Info" : {
                "Receiver Name" : receiver,
                "Authority" : authority,
                "Company Phone" : company_phone,
                "Company GSM" : company_gsm,
                "Company Adress" : company_adress
            },
            "Shipping Info" : {
                "Shipper Name" : shipper_name,
                "Customer Code": customer_code,
                "Shipping Type" : ship_type,
                "Shipper Phone" : ship_phone,
                "Shipper Adress":ship_adress
            },
            "Order Details" : {}
        }
        rowCount = self.order.ui.table_details.rowCount()
        print(rowCount)

        for row in range(rowCount):
            for column in range(3):
                if self.order.ui.table_details.item(row,column) is None:
                    print(f"{self.order.ui.table_details.item(row,column)} was None")
                    self.order.ui.table_details.setItem(row,column,QTableWidgetItem(""))
                else:
                    print("buldu")
        feedback = ""
        line = 1
        for row in range (rowCount):
            if self.order.ui.table_details.item(row,1) is None and self.order.ui.table_details.item(row,0) is None and self.order.ui.table_details.item(row,2) is None:
                print("skipped the row")
            elif self.order.ui.table_details.item(row,1).text() == "" and self.order.ui.table_details.item(row,0).text() == ""  and self.order.ui.table_details.item(row,2).text() == "":
                print("skipped the row")
            else:
                if self.order.ui.table_details.item(row,1).text() != "" and self.order.ui.table_details.item(row,0).text() != "" and self.order.ui.table_details.item(row,2).text() != "":
                    product_name = self.order.ui.table_details.item(row,0).text().upper()
                    color = self.order.ui.table_details.item(row,1).text()
                    meter = self.order.ui.table_details.item(row,2).text()


                    product = self.product_coll.find_one({"_id":product_name})
                    if product is not None:
                        if color in product["color_codes"]:
                            if self.isFloat(meter) == True:
                                self.order_data["Order Details"][str(line)] = {
                                    "Status": "new",
                                    "Item" : product_name,
                                    "Color" : color,
                                    "Meter" : meter,
                                    "Note"  :   "",
                                    "Delivered_at":"Henüz Teslim Edilmedi"
                                }   
                                line += 1
                                feedback += f"{str(row + 1):3}{product_name:10}{color:10}  {meter:5}MT\n"
                            else: 
                                if self.isInt(meter) == True:
                                    self.order_data["Order Details"][str(line)] = {
                                        "Status": "new",
                                        "Item" : product_name,
                                        "Color" : color,
                                        "Meter" : meter,
                                        "Note"  :   "",
                                        "Delivered_at":"Henüz Teslim Edilmedi"
                                    }

                                    line += 1
                                    feedback += f"{str(row + 1):3}{product_name:10}{color:10}  {meter:5}MT\n"  
                                else:
                                    raise Exception(f"Metre Bilgisi doğru girilmedi\n\nHatalı İşlem: {meter}\nSatır Sırası: {row+1}")
                        else:
                            raise Exception(f"Ürün Kodu Bulunamadı\n\nHatalı İşlem: {color}\nSatır Sırası: {row+1}")
                    else:
                        raise Exception(f"Ürün Bulunamadı\n\nHatalı İşlem: {product_name}\nSatır Sırası: {row+1}")
                else:
                    raise Exception(f"Detay bulunamadı\n\nSatır Sırası: {row+1}")


        if order_code is None :
            raise AttributeError
        if len(self.order_data["Order Details"]) == 0:
            raise Exception(f"Sipariş Detayı Bulunamadı")

        self.order.ui.lbl_order_code.setText(order_code)
        self.order.ui.lbl_date.setText(created_at)

        print(self.order_data)
        self.not_freeze_the_form(False)
        time.sleep(1)
        self.feedback_messageBox(order_code,"eklendi")
        self.order.close()
        self.refresh_form()
        self.not_freeze_the_form(True)
        self.order_coll.insert_one(self.order_data)
```
##### Order Notification 
After the Adding Order proccess is done, notification e-mail is sent to **operation departmant** and relevant customer if **radio button of notification** which is located ins etting form is checked.
###### Function
```python
 toList = []
ccList = []

settings = self.setting_coll.find_one({"_id":"notifications"})
for setting in settings:
    if setting == "operation_departmant":
        for adress in settings[setting]:
            toList.append(adress["mail"])
    elif setting == "executive":
        for adress in settings[setting]:
            ccList.append(adress["mail"])
    elif setting == "customer_service":
        for adress in settings[setting]:
            ccList.append(adress["mail"])

customer = self.customer_coll.find_one({"_id":company})
for info in customer:
    if "mail" in info:
        if customer[info] != "":
            ccList.append(customer[info])

########## Simple Mail Formatting ############
subject = f"SİPARİŞ / ORDER : {order_code}"

intro1 = f"{'Sipariş Kodu:':20}{order_code}\n"
intro2 = f"{'Firma:':20}{company}\n"
intro3 = f"{'Sipariş Tarih:':20}{order_date}\n"
intro4 = f"{'Düzenlenme Tarih:':20}{created_at}\n"
intro5 = f"{'Düzenleyen:':20}{self.username}\n"
intros = intro1 + intro2 + intro3 + intro4 + intro5

receiver_head = f"{'ALICI BİLGİLERİ':20}\n"
receiver_info1 = f"{'Alıcı Adı:':20}{receiver}\n"
receiver_info2 = f"{'Yetkili Kişi:':20}{authority}\n"
receiver_info3 = f"{'Tel No:':20}{company_phone}\n"
receiver_info4 = f"{'GSM:':15}{company_gsm}\n"
receiver_info5 =  f"{'Adres:':20}{company_adress}\n"
receiver_infos = receiver_head + receiver_info1 + receiver_info2 + receiver_info3 + receiver_info4 + receiver_info5

shipment_head = f"{'TESLİMAT BİLGİLERİ':20}\n"
shipment_info1 = f"{'Nakliyeci Adı:':20}{shipper_name}\n"
shipment_info2 = f"{'Müşteri No:':20}{customer_code}\n"
shipment_info3 = f"{'Taşıma Tipi:':20}{ship_type}\n"
shipment_info4 = f"{'Tel No':20}{ship_phone}\n"
shipment_info5 = f"{'Adres:':20}{ship_adress}\n"
shipment_infos = shipment_head + shipment_info1 + shipment_info2 + shipment_info3 + shipment_info4 + shipment_info5

body = "\n" + intros + "\n\n" + feedback + "\n\n" + receiver_infos + "\n" + shipment_infos

self.send_notification(toList,ccList,subject,body)
```
######  Sample Notification E-Mail
![order_mail](https://user-images.githubusercontent.com/69144354/150286826-22d4a8b3-91da-4ac2-adb9-37630435a688.png)


#### Generating & Ordering Order Codes
###### Algorithm
Order codes must be unique. At the same time, the codes should give the user an idea about the details of the order. For this reason, each time an order is entered, an order code that is different but contains information such as **Company Name** and **Date** should be generated.
```
Order Code = First 3 Letter Of the Company Name + Date + Amount of Repeat
```
However, some customers may want to add the codes they have determined to the order code in order to track the work. In order to respond to such requests, Order & Load offers the opportunity to choose the extra order code while adding customers. 

![extra_code](https://user-images.githubusercontent.com/69144354/149934221-9714073a-d709-4565-8121-5e5cecdbfe09.jpg)

That **Extra Code** is asked with QDialog when **Save** button is clicked. In this case, if **Extra Code** is selected Order Code logic will be like below,
```
Order Code = First 3 Letter Of the Company Name + Date + Extra Code
```
###### Function
```python
def create_orderCode(self,company):
  try:
      order_date = self.order.ui.order_date.text().split(".")
      if len(order_date[0]) == 1:
          day = order_date[0] 
          order_date[0] = "0" + day
      ##### check if any other order at the same time
      repeat = 1

      for order in self.order_coll.find():
          while company[:3] + order_date[0] + order_date[1] + order_date[2][2:] + "-" + str(repeat) == order["_id"]:
              repeat +=1

      customer = self.customer_coll.find_one({"_id":company})
      isSubscribe = customer["extra_code"]
      if isSubscribe == True:
          text, ok = QInputDialog.getText(self.order,"Ek Sipariş Kodu","Kodu Gir:")
          if ok and text is not None:
                  repeat = text

      return company[:3] + order_date[0] + order_date[1] + order_date[2][2:] + "-" + str(repeat)

  except TypeError:
      print("TypeError: Company Info is None")
      self.warning_messageBox("Lütfen Firma Seçimi Yapınız!")
```


### Main Window 
Main Window is the part of the Project which is more relevant with Operation Teams in Companies. There are 4 QTable Widget Object to follow and manage orders. These tables contain New, Preparing, Waiting(Holding) and Ready orders. Before taking any action, relevant row has to be selected. Then buttons which are located besides tables will be able to start proccesses. This design based on usage of cursor. 

![main](https://user-images.githubusercontent.com/69144354/149923111-59dbb7b8-d875-4268-8980-a02a9b109007.gif)

#### Data Transfer Algorithm
Algorithm based on reading an Order's status from the Database. Thanks to this architecture data is transferred from MongoDB Cloud Service all the time. That means data is not staying in the table.
##### Stracture of the Order "Status"
An Order which is created by Order Form takes it's status as **"new"** at first when [add_order](#order-form) function is called.  Therefore, after a row selected, clicking on the **"Prepare"** button only change the status of the order. For waiting, ready and shipped order, same structure is used. <br><br>
To examine the **"status"** values **order data modelling** kept in the Database, [click on this link](#orders).

##### Load Data to QTableWidget Objects
Algortihm is based on locate the order according to it's **status**. All action updates tables because tables are cleaned and data is loaded again after any action. Shipped Orders can be seen only via Report Form.

###### Styles of Tables
Setting Columns :
```python
# New Orders
self.window.ui.table_new_order.setColumnCount(9)      
self.window.ui.table_new_order.setHorizontalHeaderLabels(("Sipariş Kodu","Firma","Kargo","Alıcı","ID","Ürün","Ürün Kodu","Metre","Not"))
self.window.ui.table_new_order.setColumnWidth(0,150)
self.window.ui.table_new_order.setColumnWidth(1,100)
self.window.ui.table_new_order.setColumnWidth(2,125)
self.window.ui.table_new_order.setColumnWidth(3,100)
self.window.ui.table_new_order.setColumnWidth(4,50)
self.window.ui.table_new_order.setColumnWidth(5,100)
self.window.ui.table_new_order.setColumnWidth(6,100)
self.window.ui.table_new_order.setColumnWidth(7,50)
self.window.ui.table_new_order.setColumnWidth(8,175)

# Preparing Orders
self.window.ui.table_preparing.setColumnCount(5)      
self.window.ui.table_preparing.setHorizontalHeaderLabels(("Sipariş Kodu","ID","Ürün","Ürün Kodu","Metre"))
self.window.ui.table_preparing.setColumnWidth(0,75)
self.window.ui.table_preparing.setColumnWidth(1,10)
self.window.ui.table_preparing.setColumnWidth(2,100)
self.window.ui.table_preparing.setColumnWidth(3,100)
self.window.ui.table_preparing.setColumnWidth(4,10)

# Waiting Orders
self.window.ui.table_waiting.setColumnCount(5)      
self.window.ui.table_waiting.setHorizontalHeaderLabels(("Sipariş Kodu","ID","Ürün","Ürün Kodu","Metre"))
self.window.ui.table_waiting.setColumnWidth(0,75)
self.window.ui.table_waiting.setColumnWidth(1,10)
self.window.ui.table_waiting.setColumnWidth(2,100)
self.window.ui.table_waiting.setColumnWidth(3,100)
self.window.ui.table_waiting.setColumnWidth(4,10)

# Ready Orders
self.window.ui.table_ready.setColumnCount(9)      
self.window.ui.table_ready.setHorizontalHeaderLabels(("Sipariş Kodu","Firma","Kargo","Alıcı","ID","Ürün","Ürün Kodu","Metre","Not"))
self.window.ui.table_ready.setColumnWidth(0,150)
self.window.ui.table_ready.setColumnWidth(1,100)
self.window.ui.table_ready.setColumnWidth(2,125)
self.window.ui.table_ready.setColumnWidth(3,100)
self.window.ui.table_ready.setColumnWidth(4,50)
self.window.ui.table_ready.setColumnWidth(5,75)
self.window.ui.table_ready.setColumnWidth(6,100)
self.window.ui.table_ready.setColumnWidth(7,100)
self.window.ui.table_ready.setColumnWidth(8,175)
```
Setting Rows  :
```python
newOrder_rowCount = 0
preparingOrder_rowCount = 0
waitingOrder_rowCount = 0
readyOrder_rowCount = 0
shippedOrder_rowCount = 0

for order in self.order_coll.find():
    for order_items in order["Order Details"]:
        if order['Order Details'][order_items]['Status'] == "new":
            newOrder_rowCount += 1
        elif order['Order Details'][order_items]['Status'] == "preparing":
            preparingOrder_rowCount += 1
        elif order['Order Details'][order_items]['Status'] == "waiting":
            waitingOrder_rowCount += 1
        elif order['Order Details'][order_items]['Status'] == "ready":
            readyOrder_rowCount += 1
        elif order['Order Details'][order_items]['Status'] == "shipped":
            shippedOrder_rowCount += 1

self.window.ui.table_new_order.setRowCount(newOrder_rowCount)
self.window.ui.table_preparing.setRowCount(preparingOrder_rowCount)
self.window.ui.table_waiting.setRowCount(waitingOrder_rowCount)
self.window.ui.table_ready.setRowCount(readyOrder_rowCount)
```
###### Filtration 
```python
newOrder_rowIndex = 0
preparingOrder_rowIndex = 0
waitingOrder_rowIndex = 0
readyOrder_rowIndex = 0

for order in self.order_coll.find():
    for order_items in order["Order Details"]:
        if order['Order Details'][order_items]['Status'] == "new":
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,0,QTableWidgetItem(order['_id']))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,1,QTableWidgetItem(order['Company Name']))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,2,QTableWidgetItem(order["Shipping Info"]["Shipper Name"]))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,3,QTableWidgetItem(order["Receiver Info"]["Receiver Name"]))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,4,QTableWidgetItem(order_items))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,5,QTableWidgetItem(order['Order Details'][order_items]['Item']))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,6,QTableWidgetItem(order['Order Details'][order_items]['Color']))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,7,QTableWidgetItem(order['Order Details'][order_items]['Meter']))
            self.window.ui.table_new_order.setItem(newOrder_rowIndex,8,QTableWidgetItem(order['Order Details'][order_items]['Note']))
            newOrder_rowIndex += 1

        elif order['Order Details'][order_items]['Status'] == "preparing":
            self.window.ui.table_preparing.setItem(preparingOrder_rowIndex,0,QTableWidgetItem(order['_id']))
            self.window.ui.table_preparing.setItem(preparingOrder_rowIndex,1,QTableWidgetItem(order_items))
            self.window.ui.table_preparing.setItem(preparingOrder_rowIndex,2,QTableWidgetItem(order['Order Details'][order_items]['Item']))
            self.window.ui.table_preparing.setItem(preparingOrder_rowIndex,3,QTableWidgetItem(order['Order Details'][order_items]['Color']))
            self.window.ui.table_preparing.setItem(preparingOrder_rowIndex,4,QTableWidgetItem(order['Order Details'][order_items]['Meter']))
            preparingOrder_rowIndex += 1

        elif order['Order Details'][order_items]['Status'] == "waiting":
            self.window.ui.table_waiting.setItem(waitingOrder_rowIndex,0,QTableWidgetItem(order['_id']))
            self.window.ui.table_waiting.setItem(waitingOrder_rowIndex,1,QTableWidgetItem(order_items))
            self.window.ui.table_waiting.setItem(waitingOrder_rowIndex,2,QTableWidgetItem(order['Order Details'][order_items]['Item']))
            self.window.ui.table_waiting.setItem(waitingOrder_rowIndex,3,QTableWidgetItem(order['Order Details'][order_items]['Color']))
            self.window.ui.table_waiting.setItem(waitingOrder_rowIndex,4,QTableWidgetItem(order['Order Details'][order_items]['Meter']))
            waitingOrder_rowIndex += 1

        elif order['Order Details'][order_items]['Status'] == "ready":
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,0,QTableWidgetItem(order['_id']))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,1,QTableWidgetItem(order['Company Name']))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,2,QTableWidgetItem(order["Shipping Info"]["Shipper Name"]))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,3,QTableWidgetItem(order["Receiver Info"]["Receiver Name"]))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,4,QTableWidgetItem(order_items))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,5,QTableWidgetItem(order['Order Details'][order_items]['Item']))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,6,QTableWidgetItem(order['Order Details'][order_items]['Color']))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,7,QTableWidgetItem(order['Order Details'][order_items]['Meter']))
            self.window.ui.table_ready.setItem(readyOrder_rowIndex,8,QTableWidgetItem(order['Order Details'][order_items]['Note']))
            readyOrder_rowIndex += 1

self.window.ui.txt_lastUpdate.setText(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
```
#### Functions of QPushButton Objects
As it mentioned,a row has to be selected before action and Algorithm is based on changing the status of an order. Therefore, there are two common proccess implementing everytime a button is clicked. These are shared below.
##### Get Selected Item On Tables
```python
index = tableWidget.currentRow()
order_code = tableWidget.item(index,orderCode_col_index)
item_id = tableWidget.item(index,id_col_index)

if order_code is not None and item_id is not None:
    return order_code.text(), item_id.text()
else:
    print("not selected properly")
```
##### Update Order Status
```python
try:
    query = {"_id": order_code}
    new_value = {"$set": { f"Order Details.{item_id}.Status" : status}}

    self.order_coll.update_one(query, new_value)
except  pymongo.errors.PyMongoError:
    self.warning_messageBox("İnternet bağlantınızı kontrol ediniz!")   
```
##### Start to Prepare a New Order
```python
order_code, item_id = self.get_selected_item_on_table(self.window.ui.table_new_order, 0,4)
print(f"seçilen order code :{order_code} seçilen id {item_id}")
self.update_order_status(order_code, item_id, "preparing")
self.feedback_messageBox(f"{order_code}/{item_id} hazırlanmaya başladı.")
self.load_data_to_windows()
```
##### Drop a Note to an Order
```python
order_code, item_id = self.get_selected_item_on_table(self.window.ui.table_new_order, 0, 4)
print(f"seçilen order code :{order_code} seçilen id {item_id}")
try:       
    note , ok = QInputDialog.getText(self.window,"Not Ekle","Not",QLineEdit.Normal)
    if note and ok is not None:
        query = {"_id": order_code}
        new_value = {"$set": { f"Order Details.{item_id}.Note" : note}}
        self.order_coll.update_one(query, new_value)

        self.feedback_messageBox(f"{order_code}/{item_id} not eklendi.\n\nNot: {note}")
    self.load_data_to_windows()

except  pymongo.errors.PyMongoError:
    self.warning_messageBox("İnternet bağlantınızı kontrol ediniz!")
```
##### Take an Order to Wait
In case of waiting shows a problem on supplying the item. It might be out of stuck or needed more information from the customer. Therefore, any other departmant than Operation has to take action about this situation. To make this proccess easier, this project offers a simple network solution. It will be better to describe it ordered. 

**After Row Selection and Click on the Button of "Take it to Wait",**
1.  Program is asking for reason why has it taken to waiting via QtDialogWidget .
2.  Program automatically sends a notification via e-mail to mail adresses assigned as "Supplying Departmant" and "Executive"

For Modelling of the Notification Data, [click on this link](#notifications)

###### Notification Function 
```python
toList = []
ccList = []

settings = self.setting_coll.find_one({"_id":"notifications"})
for setting in settings:
    if setting == "supplying_departmant":
        for adress in settings[setting]:
            toList.append(adress["mail"])
    elif setting == "executive":
        for adress in settings[setting]:
            toList.append(adress["mail"])

subject = f"{order_code} / {item_id} BEKLEYENE ALINDI"
line = f"Aşağıda belirtilen ürün beklemeye alındı,\n\n{cause.capitalize()}.\n\n"
body =  line + f"{item_name.text()} {item_color.text()}  {item_meter.text()} MT"

self.send_notification(toList,ccList,subject,body)
```
###### Example Notification E-Mail
![waiting_order_mail-edit](https://user-images.githubusercontent.com/69144354/150127561-054fb3df-9f68-48c3-961d-bf5e6848e1d7.png)

3.  In the document of relevant product, 3 more field is added,
    - "Waiting Cause"
    - "Waiting Info"
    - "Info_by"
  
 ###### Function
 ```python
cause , ok = QInputDialog.getText(self.window,"Bekleyene Al","Bekleme Sebebi",QLineEdit.Normal)
if cause and ok is not None:
    order_code, item_id = self.get_selected_item_on_table(self.window.ui.table_new_order, 0, 4)
    self.update_order_status(order_code, item_id, "waiting")
    query = {"_id": order_code}
    new_value = {"$set": { f"Order Details.{item_id}.Waiting_cause" : cause,
                            f"Order Details.{item_id}.Waiting_info" : "",
                            f"Order Details.{item_id}.Info_by" : ""
    }}
    self.order_coll.update_one(query, new_value)
 ```
 4. After **Supplying Departmant** or **Executives** takes the necessary actions, they can add info via button named **"Add Info"**  
 5. According to info, it is  **Operation Departmant**'s turn to take action accordingly.
 
 ##### Splitting the Order
 Thanks to Data Modelling of the Products, even items of the order are taken together, program gives a chance to take action item by item. However, sometimes it may be not enough to deliver an order 10 pieces of Product A when there are only 5 so splitting is critical feature for Business Intelligence Software. 
 
 **Note:** Please be aware of that program is designed to give service to a Textile Company. That kind of companies sell fabrics meter by meter which is stocked as rolls. For example, Product A is waiting as roll of 50 Meter. When the amount of the fabric is only 5, that means 5 meters should be cutted from the whole roll.
 
 ###### Getting the Instructions
 Splitting is important proccess but having the details of the splitted items from user is also as complicated as cutting the piece. <br><br>
 Therefore, questions shared below has to be able find an answer. 
 -  How Many pieces should it split to?
 -  What are the lenght/amount of the new pieces?
 -  Is the sum of new pieces equals to their mother?
 -  Is the input send proper type of data?
 
 ```python
 try:
print("split order fonksyionu çalıştı")
index = self.window.ui.table_preparing.currentRow()
order_code = self.window.ui.table_preparing.item(index,0).text()
item_id = self.window.ui.table_preparing.item(index,1).text()
item_name = self.window.ui.table_preparing.item(index,2).text()
item_color = self.window.ui.table_preparing.item(index,3).text()
item_meter = self.window.ui.table_preparing.item(index,4).text()

dialog = self.Dialog(self.window)
piece_amount , ok = dialog.return_params("Parçala", "Kaç Parçaya Bölünecek")
if piece_amount and ok is not None:
    print(f"{piece_amount} parçaya bölünecek")
    if self.isInt(piece_amount) == True:
        repeat = 0
        pieces = []
        total_meter = 0
        while repeat < int(piece_amount):
            line = ""
            total_line = ""
            total = 0

            for i in range(len(pieces)):
                if len(pieces) != 0:
                    line += f"{i+1}.Parça :{pieces[i]}\n"
                    total += pieces[i]
                    total_line = f"Kesilen Parçalar Toplamı:{total} MT"

            piece_meter , ok = dialog.return_params("Parçala",f"{line}\n{total_line}\n\nAna Parça:{item_meter} MT\n\n{repeat+1}.Parça(MT)")
            if piece_meter and ok is not None:
                if self.isInt(piece_meter) == True:
                    pieces.append(int(piece_meter))
                    repeat += 1
                    total_meter += int(piece_meter)
                elif self.isFloat(piece_meter) == True:
                    pieces.append(float(piece_meter))
                    repeat += 1
                    total_meter += float(piece_meter)
                else:
                    self.warning_messageBox("Lütfen Sayı Giriniz.")
            else:
                dialog.close()
                break
        print(total)
        print(pieces)
    else:
        self.warning_messageBox("Lütfen Tam Sayı Giriniz.")
        print("Lütfen tam sayı giriniz.")
        dialog.close()
else:
    print("kapanıyor")
    dialog.close()
except Exception:
pass
 ```
**Note:** Input is coming via a Dialog Object which is assigned as a Class of the child of the App Class.
 
 ###### How to Split
 Function checks the data type with Exception.
 ```python
 try:

    if total_meter != int(item_meter):
        self.warning_messageBox("Parçaların toplam miktarı Ana toplam ile tutmuyor!\n\nLütfen tekrar deneyiniz.")
    else:

        # To find Order Note for splitted items
        filter = {"_id": order_code}
        order = self.order_coll.find_one(filter)
        order_note = order["Order Details"][item_id]["Note"]
        feedback = f"Ana Parça : {order_code}/{item_id} : {item_meter} MT\n\n"

        for i in range(len(pieces)):
            print(f"Order Code: {order_code} Item Id: {item_id} Item: {item_name} Color: {item_color} Meter {pieces[i]}")

            query = {"_id": order_code}
            new_value = {"$set": { 
                                f"Order Details.{item_id + '-' + str(i+1)}.Status" : "preparing",   
                                f"Order Details.{item_id + '-' + str(i+1)}.Item" : item_name,
                                f"Order Details.{item_id + '-' + str(i+1)}.Color" : item_color,
                                f"Order Details.{item_id + '-' + str(i+1)}.Meter" : str(pieces[i]),
                                f"Order Details.{item_id + '-' + str(i+1)}.Note" : order_note,
                                f"Order Details.{item_id + '-' + str(i+1)}.Delivered_at" : "Henüz Teslim Edilmedi"
            }}
            feedback += f"Parça {i+1} : {str(pieces[i])} MT\n"
            self.order_coll.update_one(query, new_value)

        self.order_coll.update_one({"_id":order_code},{"$unset":{f"Order Details.{item_id}":""}})  
        self.feedback_messageBox(feedback + "\nşekilde parçalandı.")
    self.load_data_to_windows()

except ValueError:
    if total_meter != float(item_meter):
         self.warning_messageBox("Parçaların toplamı Ana Parçadan daha fazla!\n\nLütfen tekrar deneyiniz.")
    else:
         # To find Order Note for splitted items
        filter = {"_id": order_code}
        order = self.order_coll.find_one(filter)
        order_note = order["Order Details"][item_id]["Note"]
        feedback = f"Ana Parça : {order_code}/{item_id} : {item_meter} MT\n\n"

        for i in range(len(pieces)):
            print(f"Order Code: {order_code} Item Id: {item_id} Item: {item_name} Color: {item_color} Meter {pieces[i]}")

            query = {"_id": order_code}
            new_value = {"$set": { 
                                f"Order Details.{item_id + '-' + str(i+1)}.Status" : "preparing",   
                                f"Order Details.{item_id + '-' + str(i+1)}.Item" : item_name,
                                f"Order Details.{item_id + '-' + str(i+1)}.Color" : item_color,
                                f"Order Details.{item_id + '-' + str(i+1)}.Meter" : str(pieces[i]),
                                f"Order Details.{item_id + '-' + str(i+1)}.Note" : order_note,
                                f"Order Details.{item_id + '-' + str(i+1)}.Delivered_at" : "Henüz Teslim Edilmedi"
            }}
            feedback += f"Parça {i+1} : {str(pieces[i])} MT\n"
            self.order_coll.update_one(query, new_value)

        self.order_coll.update_one({"_id":order_code},{"$unset":{f"Order Details.{item_id}":""}}) 
        self.feedback_messageBox(feedback + "\nolacak şekilde parçalandı.")
    self.load_data_to_windows()
except  pymongo.errors.PyMongoError:
    self.warning_messageBox("İnternet bağlantınızı kontrol ediniz!")
except Exception:
    pass
 ```
#### Double Click Event on Tables
All rows on tables are responsive to double click event. For this kind of feature detecting mechanism which is signal-slot connection and a QMessageBox Object is needed. 
##### Signal - Slot Connection
These connections are assigned table by table because that message box reaching details from tables. Moreover, tables are designed with different amount of columns.
```python
self.window.ui.table_new_order.doubleClicked.connect(self.doubleClick_onNew)
self.window.ui.table_preparing.doubleClicked.connect(self.doubleClick_onPre)
self.window.ui.table_waiting.doubleClicked.connect(self.doubleClick_onWait)
self.window.ui.table_ready.doubleClicked.connect(self.doubleClick_onRdy)
```
As an example for all tables,
```python
def doubleClick_onWait(self):
    order_code, item_id = self.get_selected_item_on_table(self.window.ui.table_waiting, 0,1)
    self.double_click_messageBox(order_code,item_id)
```
##### QMessageBox Object Design
```python
order = self.order_coll.find_one({"_id":order_code})
order_status = order["Order Details"][item_id]["Status"]
order_item = order["Order Details"][item_id]["Item"]
order_color = order["Order Details"][item_id]["Color"]
order_meter = order["Order Details"][item_id]["Meter"]
order_note = order["Order Details"][item_id]["Note"]
if order_status == "waiting":
    waiting_cause = order["Order Details"][item_id]["Waiting_cause"]
    waiting_info = order["Order Details"][item_id]["Waiting_info"]
    info_by = order["Order Details"][item_id]["Info_by"]
    line  = f"\nBekleme Sebebi : {waiting_cause}\nBilgi Notu : {waiting_info}\nBilgi Ekleyen : {info_by}\n"
else:
    line = ""
creater = order["Crated_by"]
order_receiver = order["Receiver Info"]["Receiver Name"]
order_receiver_authority = order["Receiver Info"]["Authority"]
order_receiver_gsm = order["Receiver Info"]["Company GSM"]
order_receiver_adress = order["Receiver Info"]["Company Adress"]
order_shipper = order["Shipping Info"]["Shipper Name"]
order_customer_code = order["Shipping Info"]["Customer Code"]
order_shipping_type = order["Shipping Info"]["Shipping Type"]
order_shipping_phone = order["Shipping Info"]["Shipper Phone"]
order_shipping_adress = order["Shipping Info"]["Shipper Adress"]

if order_status == "new":
    order_status = "Yeni Sipariş"
elif order_status == "preparing":
    order_status = "Hazırlanan Sipariş"
elif order_status == "waiting":
    order_status = "Bekleyen Sipariş"
elif order_status == "ready":
    order_status = "Tamamlanan Sipariş"
elif order_status == "delivered":
    order_status = "Sevkedilmiş Sipariş"


order_details = f"SİPARİŞ DETAYLARI\n\nSipariş Kodu : {order_code}\nDüzenleyen : {creater}\nSipariş ID : {item_id}\n\nDurum : {order_status}{line}\nÜrün : {order_item}\nRenk : {order_color}\nMetre : {order_meter}\nNot : {order_note}\n\n\n"
receiver_details = f"ALICI BİLGİLERİ\n\nAdı : {order_receiver}\nYetkili Kişi : {order_receiver_authority}\nGSM : {order_receiver_gsm}\nAdres : {order_receiver_adress}\n\n\n"
shipper_details = f"TESLİMAT BİLGİLERİ\n\nNakliyeci Adı : {order_shipper}\nMüşteri Kodu : {order_customer_code}\nTaşıma Tipi : {order_shipping_type}\nTel No: : {order_shipping_phone}\nAdres : {order_shipping_adress}\n\n\n"

msg = QMessageBox()
msg.setWindowTitle("Detay")
msg.setText(order_details + receiver_details + shipper_details)
msg.setIcon(QMessageBox.Information)
msg.setStandardButtons(QMessageBox.Ok)
msg.setWindowIcon(QtGui.QIcon('icon.png'))
msg.raise_()
x = msg.exec_()
```

### Report Form
There are two important feature that creates the Report Form to consider. One of them is Display Settings. Users are able to choose to observe the reports with the details they want to see together. Other feature is can be described as Filtering Orders as they wish. In this section these two features will be discussed with the code behind it. 

![report](https://user-images.githubusercontent.com/69144354/149923139-d512d177-0763-423c-a85e-33d1063c7cc6.gif)

#### Creating a Dynamic Structure 

##### Storage of Some Useful Datas
Only undynamic part of the Report Form is shared below. This data represent some important details. Key of "width" is used to set default sizes of table's cells's width for each detail. For example, while 30 px is enough to display the id, order code needs more space to be read clearly. Key of "path" is helping us to remove some line of code. Excel values are used to set default sizes to cell while converting the report as a xlsx file.
```python
self.column_info  = {
                "Sipariş Kodu" : {"width": 100, "path":"_id","excel":20},
                "Firma":{"width": 100, "path":"Company Name","excel":20},
                "ID" : {"width":30,"excel":8},
                "Durum":{"width":100, "path":"Status","excel":20},
                "Ürün":{"width":100, "path":"Item","excel":20},
                "Renk Kodu": {"width":100, "path":"Color","excel":12},
                "Metre" :{"width":30, "path":"Meter","excel":8},
                "Alıcı" : {"width":75,"excel":20},
                "Kargo" : {"width":75,"excel":20},
                "Sipariş Tarihi":{"width":100,"path":"Order_at","excel":25},
                "Düzenlenme Tarihi":{"width":150,"path":"Created_at","excel":25},
                "Sevk Tarihi":{"width":100, "path":"Delivered_at","excel":25},
                "Not":{"width":150,"path":"Note","excel":30}
            }
```
##### Dynamic Data Holders
As a start, datas of values of selected radio buttons are kept in list such as **Selected Display Setting**. Everytime the user change a option, thanks to signal-slot connection, software is refreshing list accordingly. Please consider that selections of display settings are creating columns and selections of filter settings are creating rows.
###### Display Datas
Holding Datas of Selected Display Setting (Order Code, Product Name etc.) :
```python
self.selected_display_items = []
for button in self.ui.btnGroup_display.buttons():
    if button.isChecked() == True:
        self.selected_display_items.append(button.text())

self.ui.table_statics.setColumnCount(len(self.selected_display_items))  
self.ui.table_statics.setHorizontalHeaderLabels((item for item in self.selected_display_items))
column_index = 0

for item in self.selected_display_items:     
    self.ui.table_statics.setColumnWidth(column_index,self.column_info[item]["width"])
    column_index += 1
```
For any changing at Display Settings, Signal-Slot Connection  :
```python
self.ui.btnGroup_display.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.display_table)
```
That connection helps to  syncronize  the display detail choices.
###### Filter Datas
Holding Datas of Selected Filtration Setting (Company Name, Order Status:New,Preparing etc.) :
```python
self.selected_filter_items = []
          for button in self.ui.btnGroup_orderDetails.buttons():
              if button.isChecked() == True:
                  self.selected_filter_items.append(button.objectName()[:-12])

          rowCount = 0
          for order in self.order_coll.find():
              if self.ui.cb_company.currentText() != "":
                  if self.ui.cb_company.currentText() != order["Company Name"]:
                      continue 
              for order_items in order["Order Details"]:
                  if order['Order Details'][order_items]['Status'] in self.selected_filter_items :
                      create_date = order["Created_at"].split()[0].split("-") 
                      year, month, day = create_date
                      date = datetime.datetime(int(year), int(month), int(day))
                      if self.ui.date_start.date() <= date <= self.ui.date_end.date():
                          rowCount += 1 
          self.ui.table_statics.setRowCount(rowCount)
```
For any changing at Filtration Settings, Signal-Slot Connection  :
```python
self.ui.btnGroup_orderDetails.buttonToggled[QtWidgets.QAbstractButton, bool].connect(self.display_table)
```
That connection helps to  syncronize  the filtration detail choices.

#### Data Transferring to the Table
As rows and columns are set, managing function of the data while observing is shared below.

##### Selecting Algorithm of Quries of Rows and Columns
1. Is the item which is reached via "for" loop matching with the selected one, if it is selected from combobox?
2. Is the order's Creating Date between starting and finishing QDate objects?
    - As default, QDate objects are setting for last 1 month.
3. Is Status of the Order in list of *selected_filter_items* ?
4. Which details are choosen to set as a column? 
    - To check this info, a "for" loop is set which is comparing the order details with the items of *selected_display_items*

```python
meter = 0
record = 0

row_index = 0
for order in self.order_coll.find():
    if self.ui.cb_company.currentText() != "":
        if self.ui.cb_company.currentText() != order["Company Name"]:
            continue 
    for order_items in order["Order Details"]:
        create_date = order["Created_at"].split()[0].split("-") 
        year, month, day = create_date
        date = datetime.datetime(int(year), int(month), int(day))
        if self.ui.date_start.date() <= date <= self.ui.date_end.date():
            if order['Order Details'][order_items]['Status'] in self.selected_filter_items :

                for item in self.selected_display_items:
                    if item == "Sipariş Kodu" or item == "Firma" or item == "Düzenlenme Tarihi" or item == "Sipariş Tarihi":
                        self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem(order[self.column_info[item]["path"]]))
                    elif item == "Durum":
                        if order['Order Details'][order_items]['Status'] == "new":
                            self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem("YENİ"))
                        elif order['Order Details'][order_items]['Status'] == "preparing":
                            self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem("HAZIRLANAN"))
                        elif order['Order Details'][order_items]['Status'] == "waiting":
                            self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem("BEKLEYEN"))
                        elif order['Order Details'][order_items]['Status'] == "ready":
                            self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem("TAMAMLANAN"))
                        elif order['Order Details'][order_items]['Status'] == "delivered":
                            self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem("SEVKEDİLEN"))
                    elif item == "ID":
                        self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem(order_items))
                    elif item == "Ürün" or item == "Renk Kodu" or item == "Metre" or item == "Not" or item == "Sevk Tarihi":
                        self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem(order['Order Details'][order_items][self.column_info[item]["path"]]))
                        if item == "Metre":
                            try:
                                meter += int(order['Order Details'][order_items][self.column_info[item]["path"]])
                            except ValueError:
                                meter += float(order['Order Details'][order_items][self.column_info[item]["path"]])
                    elif item == "Alıcı":
                        self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem(order["Receiver Info"]["Receiver Name"]))
                    elif item == "Kargo":
                        self.ui.table_statics.setItem(row_index,self.selected_display_items.index(item),QTableWidgetItem(order["Shipping Info"]["Shipper Name"]))

                row_index += 1
                record += 1 
                self.rowIndex = row_index

self.ui.lbl_amount.setText("Toplam Metre :")
self.ui.lbl_txt_amount.setText(str(meter)+" MT")
self.ui.lbl_record.setText("Toplam Kayıt :")
self.ui.lbl_txt_record.setText(str(record))
```
#### Converting as Excel File

##### Selecting Algorithm of Rows and Columns
1.  Open a Excel File.
2.  Set Column widths the size which is set with *self.column_info* dictionary.
3.  Set same amount of Row with the variable of *self.rowIndex*.
4.  Set same amount of Column with the lenght of *selected_display_items*.
5.  If Column is "Meter", reformat it as a integer type of data.
6.  Set a Random Code for the document.
7.  Save the file to selected path with file browser.

Users are able to convert the data as they have seen on QTableWidget. Choosen Column details may change according to user's needs so this structure also has to be dynamic as well as rest of the code of the Report Form. Thanks to data holder list that we assigned above helps to do that quickly.

```python
def convert_excel(self):   
try:
    wb = Workbook()
    ws = wb.active
    ws.title = "Order & Load Report"
    headings = self.selected_display_items
    ws.append(headings)

    for col in range(len(self.selected_display_items)):
        ws[get_column_letter(col+1) + "1"].font = Font(bold=True)
        ws.column_dimensions[get_column_letter(col+1)].width = self.column_info[self.selected_display_items[col]]["excel"]

    for row in range(self.rowIndex):
        row_data = []
        for column in range(len(self.selected_display_items)):
            if self.selected_display_items[column] == "Metre":
                try:
                    formatted_meter = int(self.ui.table_statics.item(row,column).text())
                    row_data.append(formatted_meter)
                except ValueError:
                    formatted_meter = float(self.ui.table_statics.item(row,column).text())
                    row_data.append(formatted_meter)
            else:
                row_data.append(self.ui.table_statics.item(row,column).text())
        ws.append(row_data)

    filecode = random.randint(1,10000000000)
    dir_path = QFileDialog.getExistingDirectory()
    print(type(dir_path))
    print(dir_path)
    if dir_path != "":
        wb.save(dir_path + f"/O&L-{filecode}.xlsx")

        msg = QMessageBox()
        msg.setWindowTitle("İşlem Raporu")
        msg.setText(f" Dosya {f'/O&L-{filecode}.xlsx'} oluşturuldu.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.raise_()
        x = msg.exec_()

except Exception as ex :
    msg = QMessageBox()
    msg.setWindowTitle("Uyarı")
    msg.setText(f"Hata: {ex}")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QtGui.QIcon('icon.png'))
    msg.raise_()
    x = msg.exec_() 
```

## Server Application
The main purpose of the Server Application is to send a report which contains daily loadings to the relevant customers at the end of the day.
For this reason, **timer**, **filter**, **recorder** and **notifier** functions in this application are important. We will evaluate this application under these headings.

![server](https://user-images.githubusercontent.com/69144354/149890024-821fbed0-1021-4442-94a5-f3c1ff1ac4f4.gif)

##### Timer
It is necessary to wait for the end of the shift at least in order to transmit the daily reports. It is necessary to have at least one timer to wait for the end of the shift.
```python
from PyQt5.QtCore import QTimer, QTime
from datetime import datetime, date

class ServerWidget(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        super(ServerWidget,self).__init__()
        
        timer = QTimer(self)
        timer.timeout.connect(self.display_time)
        timer.start(1000)  
        
    def set_time(self):
        self.today = date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.this_date_object = datetime(int(self.year), int(self.month),int(self.day-1),int(18))
        self.now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Now
        
    def check_time(self):
        self.set_time()
        if self.ui.txt_time.text() == "18:00:00":
            self.write_on_records("Time is matched to send loading reports.")
            self.send_reports()
    
```
##### Filter
This is crucial to have an efficient filtering function that first separates customers from each other, then separates the shipped from all orders, and now separates the shipped from all.
```python
loading_count = 0
for company in self.customer_coll.find(): # Call customers one by one to filter
    delivered_items = []
    for order in self.order_coll.find():
        if order["Company Name"] == company["_id"]: # Reaching relevant customer's orders
            counter = 1
            for order_items in order["Order Details"]:
                if order['Order Details'][order_items]['Delivered_at'] != "Not Shipped Yet": # Filtering Shipped Orders than other orders
                    deliver_date = order['Order Details'][order_items]['Delivered_at']
                    deliver_date_object = datetime.strptime(deliver_date, '%Y-%m-%d %H:%M:%S')
                    if deliver_date_object >= self.this_date_object:                         # Filtering Shipped Orders which is made today from all shipped orders
                        cargo_recevier = f"LOADING ID: {counter}\nCARGO: {order['Shipping Info']['Shipper Name']}  RECEIVER: {order['Receiver Info']['Receiver Name']}\n"
                        delivered_items.append(f"{cargo_recevier}{order['_id']}/{order_items}: {order['Order Details'][order_items]['Item']} {order['Order Details'][order_items]['Color']} {order['Order Details'][order_items]['Meter']} MT") 
                        counter += 1 
```
##### Recorder
This application is basically designed to work on its own,that is why it is very important to keep records to ensure that it works correctly or to be aware of errors.
However, we cannot be completely sure how the errors will occur so it would be more accurate to keep these records both locally and in the cloud. For example, if we only kept logs in the cloud, we would not be aware of errors related to queries.
```python
def write_on_records(self, record):
    print(record)
    with open("records.txt","r+", encoding="utf-8") as file:
            content = file.read()
            content = content + "\n" + f"{str(self.now)}: " + record
            file.seek(0)
            file.write(content) 

    self.setting_coll.update_one({"_id":"server_log"},{"$push":{"records" :str(self.now)+ " " + str(record)}}) 
    self.setting_coll.update_one({"_id":"server_log"},{"$set":{"last_seen":str(self.now)}})
```
###### Outputs:
###### records.txt
```txt
2021-12-30 21:32:22: Failed while sending loading report to Company 1! Error:send_notification() takes 3 positional arguments but 5 were given.
2021-12-30 21:32:22: Application is closed.
2021-12-30 21:36:46: Application is closed.
2021-12-30 21:37:11: Information of the Loading of 1 item succesfully sent to Company 1.
2021-12-30 21:37:11: Information of the Loading of 1 item succesfully sent to Company 2.
2021-12-30 21:37:11: Information of the Loading of 1 item succesfully sent to Company 3.
2021-12-30 21:37:11: Application is closed.
2021-12-30 21:58:37: Application is activated.
2021-12-30 21:58:37: Information of the Loading of 1 item succesfully sent to Company 2.
2021-12-30 21:58:37: Information of the Loading of 1 item succesfully sent to Company 5.
2021-12-30 21:58:37: Information of the Loading of 1 item succesfully sent to Comapny 6.
2021-12-30 21:58:37: Application is closed.
2021-12-31 13:04:56: Application is activated.
2021-12-31 13:04:56: Application is tested.
2021-12-31 13:04:56: Application is closed.
```
To see the output at the Cloud, click this link [Server Log](#server-log)

##### Notifier
In order for it to continue its function stably, we need to be instantly aware of any errors that may occur. Possible error and close events are sent to the technical team with the notification function.
```python
def send_notification(self,subject,body):
    try:
        setting = self.setting_coll.find_one({"_id":"notifications"})
        From = setting["admin"][0]["mail"]
        Password = setting["admin"][0]["password"]

        toList = []
        ccList = []

        settings = self.setting_coll.find_one({"_id":"notifications"})
        for setting in settings:
            if setting == "executive":
                for adress in settings[setting]:
                    ccList.append(adress["mail"])
            elif setting == "technic":
                for adress in settings[setting]:
                    toList.append(adress["mail"])

        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = From
        msg["To"] = ",".join(toList)
        msg["Cc"] = ",".join(ccList)

        context=ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg["From"], Password)
            smtp.send_message(msg)

    except Exception as ex:
        self.write_on_records(f"Error occured while sending notification to technic: {ex}")
```
###### Examples For Usage
In case of Reporting Loadings :
After Loading datas are filtered, function shared below is starting to work.
```python
if len(delivered_items)  > 0:
toList = []
ccList = []

customer = self.customer_coll.find_one({"_id":company["_id"]})
for info in customer:
    if "mail" in info:
        if customer[info] != "":
            toList.append(customer[info])

settings = self.setting_coll.find_one({"_id":"notifications"})
for setting in settings:
    if setting == "executive":
        for adress in settings[setting]:
            ccList.append(adress["mail"])

subject = f"LOADING REPORT: {company['_id']} {self.day}{self.month}{str(self.year)[-2:]}"
body = "Hello,\n\nThe details of your loading done today are shared below,\n\n\n"
for item in delivered_items:
    body += (item + "\n\n")
body += "\n\nPlease do not reply this e-mail."

self.send_notification_to_customer(toList,ccList,subject,body)
```
In case of Error  :
```python
except Exception as ex:
        self.write_on_records(f"Failed while sending loading report to {company['_id']}! Error:{ex}.")
        subject = "ERROR OCCURED AT THE SERVER"
        body = f"Hello,\n\nError is shared below,\n{ex}\n\nLast Seen: {self.now}\n\n\nPlease do not reply this e-mail."
        self.send_notification(subject,body)
```
In case of Unexpected Exit  :
```python
def closeEvent(self,event):
    subject = "APPLICATION OF ORDER & LOAD IS CLOSED AT THE SERVER"
    body = f"Hello,\n\nClose Event of the App is activated.\nLast Seen: {self.now}\n\nPlease do not reply this e-mail."
    self.send_notification(subject,body)
    self.write_on_records("Close Event of the Server App is successfully activated.")
```
###### Sample Notification E-Mails  
###### Loading Report : 
![report_mail](https://user-images.githubusercontent.com/69144354/150288382-d2bc98c2-4fe0-4ca2-a8cc-5e5c8a9e3570.png)

###### Error  :
![error_mail](https://user-images.githubusercontent.com/69144354/150288427-94f665a1-c900-4b7e-a3bf-e3b1bb87e4d6.png)

###### Close Event  :
![closeEvent_mail](https://user-images.githubusercontent.com/69144354/150288472-9098576a-25f3-41be-bde2-169a75fe4c74.png)

## Data Modelling

**MongoDB**, which is a NoSQL database, was preferred in the project. With this feature, MongoDB allows you to create non-relational data collections containing documents. Of course, there will always be data that needs to be associated with each other, but completing this association on the side where the queries are sent provides significant flexibility to the developers. When needed, dictionary-type data with key-value relationships, arrays or arrays of dictionary-type data can be added to the documents.
At the same time, with this structure, you can perform innovations much faster because you do not have to add the newly added fields to all the documents in the collection.
It should be added independently of the project that NoSQL databases are more preferred in projects where large volumes of data are managed.

**Note** : Since information such as Customer Name, Shipping Name, Product Name and Order Code is unique, this information is used in the **"_id"** field instead of **"ObjectId"**. Thanks to this method, queries have become easier to do.

### Connection
If the login is successful in the Username and Password entries in Login Form, takes place at the connection string displayed. Then connection to collections are completing as it seen below.
```python
self.myclient = pymongo.MongoClient(f"mongodb+srv://{username_entry}:{password_entry}@cluster0.asdnj.mongodb.net/app_test?retryWrites=true&w=majority")
self.mydb = self.myclient["order-load"]
self.customer_coll = self.mydb["customers"]
self.cargo_coll = self.mydb["cargos"]
self.order_coll = self.mydb["orders"]
self.product_coll = self.mydb["products"]
self.setting_coll = self.mydb["settings"]
```

### Customers
There is some information requested by the program when storing customer data,

| Name          | Mail 1        | Mail 2        | Mail 3        | Extra Code    | Notifications |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Company 1     | company1@...  | company1@...  |    None       | False         | True          |
| Company 2     | company2@...  | None          | None          | True          | True          |

At least the name entry is enough for the following structure to be formed on the MongoDB side.

```json
{
  "_id":"Company 2",
  "mail1":"company2@company.com",
  "mail2":"",
  "mail3":"",
  "extra_code":true,
  "notification":true
}
```
### Cargos
```json
{
  "_id":"Cargo 1",
  "authority":"James Thompson",
  "phone":"+90 212 586 86 21",
  "adress":"Hayriye Tüccarı Cad. Kızıltaş Sok. No:57/1 Nişanca/Kumkapı/ İstanbul"
}
```
### Products 
```json
{
  "_id":"Product A",
  "code":"2201.1D",
  "supplier":"Company ABC",
  "supplier_product_name":"Product A",
  "type":"Fabric",
  "usage":"Curtain",
  "width":300,
  "weight":258,
  "composition":"%72 Polyester %28 Viskon",
  "color_codes":[
      "2201.1D.78",
      "2201.1D.34",
      "2201.1D.67",
      "2201.1D.23",
      "2201.1D.28",
      "2201.1D.14",
      "2201.1D.36",
      "2201.1D.38",
      "2201.1D.55",
      "2201.1D.88",
      "2201.1D.32"
      ]
}
```
##### Synchronization of Products
Business intelligence Software should often have a database or dataset into which products are integrated.
In large-volume management information systems such as a ERP, products can also be added from the system. In this project, products were entered by using the **pandas** library from a ready dataset.

Sample Dataset which is in same format with the one used in this project can be founded in the source file.
```python
import pandas as pd
import pymongo

#   Username and Password is needed to send a request to database
username = ""
password = ""
#   File we want to sync with our database has to be shared here as a path
file = r"C:\Users\Asus\Desktop\sample_products.xlsx"

def synchronize(username,password,file,sheet_index):
    myclient = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.asdnj.mongodb.net/app_test?retryWrites=true&w=majority")
    mydb = myclient["order-load"]
    product_coll = mydb["products"]

    xl = pd.ExcelFile(file)

    data_frame1 = xl.parse(sheet_index) 
    index = data_frame1.index
    number_of_rows = len(index) 

    products = {}

    for i in range(number_of_rows):

        product_name = data_frame1["AD"][i]
        product_code = str(data_frame1["RENK KOD"][i])[:-3]
        color_code = data_frame1["RENK KOD"][i]
        width = data_frame1["EN"][i]
        composition = data_frame1["KOMPOZİSYON"][i]
        weight = data_frame1["GR/M²"][i]
        product_type = data_frame1["ÜRÜN CİNSİ"][i]
        usage = data_frame1["KULLANIM ALANI"][i]
        supplier_name = data_frame1["TEDARİKÇİ"][i]
        supplier_product_name = data_frame1["TEDARİKÇİ AD"][i]
        supplier_product_color = data_frame1["TEDARİKÇİ RENK KOD"][i]

        if product_name is not None:
            if product_name in products:
                products[product_name]["color_codes"].append({"color_code":color_code})
            else: 
                products[product_name] = {
                    "code":product_code,
                    "supplier":supplier_name,
                    "supplier_product_name":supplier_product_name,
                    "type":product_type,
                    "usage":usage,
                    "width":width,
                    "weight":weight,
                    "composition":composition,
                    "color_codes" : [{"color_code":color_code}]
                 }
        else:
            continue
        
    product_data = {}

    for product in products:
        try:
            product_data = {
                "_id" : product,
                "code":products[product]["code"],
                "supplier":products[product]["supplier"],
                "supplier_product_name":products[product]["supplier_product_name"],
                "type":products[product]["type"],
                "usage":products[product]["usage"],
                "width":products[product]["width"],
                "weight":products[product]["weight"],
                "composition":products[product]["composition"],
                "color_codes" : []
                }
            for i in range(len(products[product]['color_codes'])):
                product_data["color_codes"].append(products[product]['color_codes'][i]['color_code'])
            product_coll.insert_one(product_data)
        except pymongo.errors.DuplicateKeyError:
            continue
            
if __name__ == "__main__":
    synchronize(username,password,file,0)
    synchronize(username,password,file,1)
```

### Orders

Below is an example of **correlating data**. In the Company Name field, **customers** collection must match the information in the **"_id"** field. This matching takes place when the order is entered. The same applies to cargo and product informations.

```json
{
  "_id":"COM100122-2",
  "Company Name":"Company 1",
  "Crated_by":"cuneyttopbas",
  "Created_at":"2022-01-10 13:32:20",
  "Order_at":"10.01.2022",
  "Receiver Info":{
      "Receiver Name":"ABC Textile Co.",
      "Authority":"Hannah Simpson",
      "Company Phone":"+90 530 0354 6",
      "Company GSM":"+25 441 25 544",
      "Company Adress":"Moscow, Russia"
      },
  "Shipping Info":{
      "Shipper Name":"Cargo 1 ",
      "Customer Code":"690",
      "Shipping Type":"Air Shipment",
      "Shipper Phone":"+452 22 4 5 55 ",
      "Shipper Adress":"Neslişah Mah. Vatan Cad. Banka Evleri C1 Blok No 82/1 Fatih"
      },
  "Order Details":{
      "1":{
          "Status":"delivered",
          "Item":"Product A",
          "Color":"2201.1D.78",
          "Meter":"35",
          "Note":"Free of Charge",
          "Delivered_at":"2022-01-11 16:41:14"
          },
      "2":{
        "Status":"new",
        "Item":"Product B",
        "Color":"1828.1D.03",
        "Meter":"1.7",
        "Note":"",
        "Delivered_at":"Not Shipped yet"
      }
      "3-1":{
        "Status":"preparing",
        "Item":"Product C",
        "Color":"1898.1D.05",
        "Meter":"10.5",
        "Note":"Be careful with this one",
        "Delivered_at":"Not Shipped yet"
      }
      "3-2":{
        "Status":"waiting",
        "Item":"Product C",
        "Color":"1898.1D.05",
        "Meter":"4.5",
        "Note":"Be careful with this one",
        "Delivered_at":"Not shipped yet",
        "Info_by" : "operation_departmant",
        "Waiting_cause" :"We dont have it now, not able to prepare!",
        "Waiting_info": "We will have it in two weeks."
      }
   }
}
```
To reinforce with an example, it has matched this information, which is actually still unrelated and consists of a string data, preventing a different selection in the user interface,

##### Matching Products while Adding an Order

```python
product = self.product_coll.find_one({"_id":product_name}) # Filter with "_id" which the name of the Product
if product is not None:
    if color in product["color_codes"]:
        if self.isFloat(meter) == True:
            self.order_data["Order Details"][str(line)] = {
                "Status": "new",
                "Item" : product_name,
                "Color" : color,
                "Meter" : meter,
                "Note"  :   "",
                "Delivered_at":"Not Shipped Yet"
            }   
```
##### Matching All Datas while Sending Loading Report at the Server side

```python

for company in self.customer_coll.find():           # Step 1-  Reaching to "customers" collection
    delivered_items = []                    
    for order in self.order_coll.find():            # Step 2-  Reaching to "orders" collection
        if order["Company Name"] == company["_id"]: # Step 3-  Matching a document's "_id" field from customers with document's "Company Name" from orders
            counter = 1
            for order_items in order["Order Details"]:
                if order['Order Details'][order_items]['Delivered_at'] != "Henüz Teslim Edilmedi":
                    deliver_date = order['Order Details'][order_items]['Delivered_at']
                    deliver_date_object = datetime.strptime(deliver_date, '%Y-%m-%d %H:%M:%S')
                    if deliver_date_object > self.this_date_object:
                        cargo_recevier = f"LOADING ID: {counter}\nCARGO: {order['Shipping Info']['Shipper Name']}  RECEIVER: {order['Receiver Info']['Receiver Name']}\n"
                        delivered_items.append(f"{cargo_recevier}{order['_id']}/{order_items}: {order['Order Details'][order_items]['Item']} {order['Order Details'][order_items]['Color']} {order['Order Details'][order_items]['Meter']} MT") 
                        counter += 1 
    if len(delivered_items)  > 0:
        toList = []
        ccList = []

        customer = self.customer_coll.find_one({"_id":company["_id"]})
        for info in customer:
            if "mail" in info:
                if customer[info] != "":
                    toList.append(customer[info])

        settings = self.setting_coll.find_one({"_id":"notifications"})
        for setting in settings:
            if setting == "executive":
                for adress in settings[setting]:
                    ccList.append(adress["mail"])

        subject = f"LOADING REPORT: {company['_id']} {self.day}{self.month}{str(self.year)[-2:]}"
        body = "Hello,\n\nThe details of your loading done today are shared below,\n\n\n"
        for item in delivered_items:
            body += (item + "\n\n")
        body += "\n\nPlease do not reply this e-mail."

        self.send_notification_to_customer(toList,ccList,subject,body)
        self.write_on_records(f"Information of the Loading of {len(delivered_items)} item succesfully sent to {company['_id']}.")
        self.load_screen()

self.write_on_records("Sending Report Process is completed.")

```
### Notifications
The program sends automatic mails at many stages. According to the subject of the stages, the people to whom the e-mail will be sent also vary.

```json
{
  "_id":"notifications",
  "operation_departmant":[
    {"mail":"operator_1@company.com"},
    {"mail":"operator_2@company.com"}
    ],
  "customer_service":[
    {"mail":"customer_service@company.com"}
    ],
  "executive":[
    {"mail":"cuneyt.topbas@company.com"},
    ],
  "supplying_departmant":[
    {"mail":"supplying@company.com"}
    ],
  "technic":[
    {"mail":"technic@company.com"}
    ],
    "admin":[
    {"mail":"admin@gmail.com","password":"Admin123"}
  ],
}
```
##### Selecting Relevant Adresses
If the Operation, Customer Service and Executive units within the company need to take action or be informed at the time of placing the order, it will be useful to create the structure below.

```python
settings = self.setting_coll.find_one({"_id":"notifications"})
for setting in settings:
    if setting == "operation_departmant":
        for adress in settings[setting]:
            toList.append(adress["mail"])
    elif setting == "executive":
        for adress in settings[setting]:
            ccList.append(adress["mail"])
    elif setting == "customer_service":
        for adress in settings[setting]:
            ccList.append(adress["mail"])
```

### Server Log
Taking advantage of Artificial Intelligence provides serious convenience in our lives. So much so that these conveniences can turn into habits over time. For this reason, stability is very important at this stage.

In order to ensure stability, it is important to be aware of errors quickly as well as to avoid errors. This can only be possible with close monitoring. In order to achieve this, it was deemed appropriate to create a structure like the one below.
```json
{
  "_id":"server_log",
  "last_seen":"2022-01-14 18:00:00",
  "records":[
      "2022-01-10 09:29:01 Database connection is activated.",
      "2022-01-10 09:29:01 Application is activated.",
      "2022-01-10 09:29:09 Application is tested successfully.",
      "2022-01-10 09:29:40 Close Event of the Server App is successfully activated.",
      "2022-01-10 09:37:15 Database connection is activated.",
      "2022-01-10 09:37:15 Application is activated.",
      "2022-01-10 18:00:00 Time is matched to send loading reports.",
      "2022-01-10 18:00:00 Sending Report Process is started.",
      "2022-01-10 18:00:00 Information of the Loading of 3 item succesfully sent to Company 1.",
      "2022-01-10 18:00:00 Sending Report Process is completed.",
      "2022-01-11 18:00:00 Time is matched to send loading reports.",
      "2022-01-11 18:00:00 Sending Report Process is started.",
      "2022-01-11 18:00:00 Information of the Loading of 8 item succesfully sent to Company 1.",
      "2022-01-11 18:00:00 Information of the Loading of 3 item succesfully sent to Company 2.",
      "2022-01-11 18:00:00 Information of the Loading of 2 item succesfully sent to Company 3.",
      "2022-01-11 18:00:00 Sending Report Process is completed.",
      "2022-01-12 18:00:00 Time is matched to send loading reports.",
      "2022-01-12 18:00:00 Sending Report Process is started.",
      "2022-01-12 18:00:00 There was no any loading today to send as a report.",
      "2022-01-12 18:00:00 Sending Report Process is completed.",
      "2022-01-13 18:00:00 Time is matched to send loading reports.",
      "2022-01-13 18:00:00 Sending Report Process is started.",
      "2022-01-13 18:00:00 Information of the Loading of 5 item succesfully sent to Company 2.",
      "2022-01-13 18:00:00 Information of the Loading of 3 item succesfully sent to Company 1.",
      "2022-01-13 18:00:00 Information of the Loading of 2 item succesfully sent to Company 5.",
      "2022-01-13 18:00:00 Sending Report Process is completed.",
      "2022-01-14 11:43:45 Database connection is activated.",
      "2022-01-14 11:43:45 Application is activated.",
      "2022-01-14 11:44:12 Close Event of the Server App is successfully activated.",
      "2022-01-14 11:44:24 Database connection is activated.",
      "2022-01-14 11:44:24 Application is activated.",
      "2022-01-14 11:44:43 Application is tested successfully.",
      "2022-01-14 11:44:49 send_records method is called from the console.",
      "2022-01-14 11:44:49 Records are sent successfully from the console.",
      "2022-01-14 11:44:55 Invalid entrance is detected at the console.",
      "2022-01-14 11:45:24 Invalid entrance is detected at the console.",
      "2022-01-14 11:45:31 Close Event of the Server App is successfully activated.",
      "2022-01-14 18:00:00 Time is matched to send loading reports.",
      "2022-01-14 18:00:00 Sending Report Process is started.",
      "2022-01-14 18:00:00 There was no any loading today to send as a report.",
      "2022-01-14 18:00:00 Sending Report Process is completed."
      ]
}
```
To go back, click this link [Recorder](#recorder)
##### Refreshing the Array of Records
Over time, the data here will grow and the old data will become meaningless. Therefore, there is a need to create a self-cleaning algorithm like the one below.
```python
 settings  = self.setting_coll.find({"_id":"server_log"})
  for setting in settings:              # Step 1- Checks the amount of line
      count = 0
      for line in setting["records"]:
          count += 1
  if count >= 50:                       
      delete_amount = count - 50          # Step 2- If amoutn is more than 50, it calculates the amount of line has to be deleted
      settings  = self.setting_coll.find({"_id":"server_log"})
      for setting in settings:
          del_rpt = 0
          for line in setting["records"]:
              if del_rpt < delete_amount: # Step 3- Unwanted(Oldest) records are pulled from the array of the records
                  self.setting_coll.update_one({"_id":"server_log"},{"$pull":{"records" : line}}) 
                  del_rpt += 1
```
## How to Convert a Project to App ?
If you are using Python Programming Language and have a cool script that you want to convert it to a Desktop Application like this one, you are at the right place! 
First of all you need to install **pyinstaller** via your **Terminal**.
```terminal
pip install pyinstaller
```
Now, you need to open the folder where your script is located with all other relevant files. Please be sure that you have the **.ico** file you want it as the icon of the App. After that, in this folder you have to click on **"Shift"** and **"Right Click"** at the same time. You must be able to see a option called **"Open PowerShell from here"**, click on it without waiting no more. I suggest you to write as I shared below.

![terminal_pyinstaller](https://user-images.githubusercontent.com/69144354/150142401-2f2edea1-6d77-47dd-af33-7761974a5450.png)
###### Configurations
```
--  one file -> Create a one-file bundled executable.
 -  w -> Windowed, no console
 -  i -> Adding a Icon 
```
For more option check the [documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).

Please consider that **main file** has to be the last one. <br><br>
Congrulations! You will find your .exe file in a folder named **"dist"**.
### Possible Errors
When I converted  my project to app, I recognized that my script was not able to find my .txt and .png files. After I relocate the them to folder which .exe file stays, It solved.<br><br>
For more possible errors check the [documentation](https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html).
## How to Contribute ? 

I am very praud to see you here! Your interest and feedbacks are kind of gift to me. If you are looking for a solution for any of your question which similar to ones shared here, I would be glad to help you.

### Develop As You Wish 

I would like to update this project with your new features and improvement. Do not hesitate to send me.

### Challenge Yourself

There are several errorr which is hidden through codes. I will share with you the ones which are discovered while using by a company. 

- [x] When it takes a order to waiting table throws an error
- [x] Server Application do not send the daily loading reports.
- [ ] After change an item from Cargo Combo box receiver line edits are updated as well.
- [ ] If "F1" pressed at Variant Code Cell which is in the Order Form, program throws an error.
- [ ] Sometimes in case of disconnection of the internet, program throws an error.
