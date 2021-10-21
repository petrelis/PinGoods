# Software Engineering project "PinGoods"
# Group II
# Technical Requirements

PinGoods is a local goods platform dedicated to easily connecting vendors with their customers.

## 1. System Representation

Our diagrams below represent main internal and external parts of the system. They let new developers to easily integrate to the project, and to be acknowledged with what needs to be developed. 

The use case matrix below represents all the key features and user roles in our project. Each row represents a key functionality, and each column represents a user role. Cells marked in green indicate that for the user, in which column he is placed, the functionality, in which row is placed, is available. Red-colored cells represent the opposite. Unauthorized user is the most restricted user role as we want to encourage users to register on our website. Although most of the features are limited to them, however, we allow them to experience our system by using our search system and viewing Vendor information. The main difference between Customer and Vendor roles is that the first is dedicated to buying and the other to selling. However, for one email account, users can still register both Customer and Vendor accounts. It is also visualized that the Vendor role is divided into two sub-roles: with and without a subscription. The subscription fee is not specified yet, but the main difference is that it allows our suppliers to sell more items, boost their products for free in search and disable ads. Finally, the Admin role has access to all key functionalities, including Customers' and Vendors'. They are responsible for checking for bugs and patrolling the website for impolite reviews. The only limitation for admins is to edit user reviews as user opinions must remain unchanged.

![Use-Case Matrix](https://user-images.githubusercontent.com/47245874/135151107-f3b1b202-6b2b-44f3-bc39-605a59cab5e9.png)

Use case diagrams to represent all-important key features more abstractly. Unauthorized users are not included because they do not have many features available. The admin role is not included for the opposite reason - it has too many features available and nothing important to mention. Subscription-free sellers are mentioned because we expect there will be fewer sellers who subscribe, so we are majority-oriented. However, one of the roles of the subscription provider is mentioned as an extension of the subscription purchase function.

![Use-Case Diagram](https://user-images.githubusercontent.com/47245874/137370247-c92db5df-895c-45e5-a4d3-b168d6251ef8.png)

This project contains many important hardware and software components. Users can connect with web browsers on their devices. All the main system files are located on the main web server, which we use Windows Server 2012 provided by the University. We chose Windows Server 2012 because we were limited with the resources we're provided. The Controller.jar script accesses the database and selects data from there, communicating with Google Host and the Paysera API for the banking simulation.

![Deployment Diagram](https://user-images.githubusercontent.com/47245874/137368741-1c94bb12-1a61-43e9-be80-ef9d7232edb6.jpg)

The interaction of our system at the high level is represented in the System Context diagram. In our project, we are going to use Google Ads, Google Maps APIs, and Paysera for simulation of banking transactions. We use Google APIs as they are the most popular and well-designed APIs for adding ads and map systems to our project. We were suggested using Paysera for simulation of banking systems, and we decided to use it instead of creating our banking system only for simulation. It'd take an additional time to work. In case, Google Maps API doesn't provide the functionality to calculate the distance between the Customer and the Vendor, then we'll write our own. Mostly, the Google Maps API is needed for the location of the Vendors. For the additional gain from the project, we're adding ads to our website. We expect to configure it in a way that is not going to bring any not user-friendly experience for our users.

![System Context Diagram](https://user-images.githubusercontent.com/47245874/137368762-f4d93add-b510-4d7a-930d-607efc3b3f16.jpg)

Looking at the entire behavior of the system would take too long and more than one diagram. We have decided to make one of the main features available to all users of our project in research activities - searching. Users have the option to browse the list of products presented when opening a search bar window or search by entering keywords and/or applying filters. If users find the product they need, they can do another search for another product or buy the one they have chosen.

![Activity Diagram](https://user-images.githubusercontent.com/47245874/137367706-4f2a6ac6-3c1e-4a22-92b6-9b8a1048bb1c.png)


## 2. The Great Gang

Each project member chose a working team in which is most comfortable. This was done to save time and improve efficiency. As a well-coordinated team, we will collaborate with the rest of the team. We selected these specific teams as a part of our project. Why? Because the big guys on the internet said these specific teams should be enough for any project. And we decided to go for it.

**Lead: Sahak Ivašauskas @sahiva**

- **Front-End**
  - **Gustas Petkevičius @FlooPeriS (Sub-Lead)**
  - Sara Sánchez @SaraSanGar
  - Danielius Miškinis @Segulx
  - Pablo Santana @pablosanttanaa
  - Liudas Kraujalis @Liudaskr
  - David Kisel @DavidK14
  - Maksym Hrynak @hrymasik
  
- **Back-End**
  - **Marius Raupelis @mariusraupel (Sub-Lead)**
  - Martynas Jakučionis @Jaku12345
  - Gustas Strimaitis @Radorkan
  - Aurimas Miliauskas @AuriTheGreat
  - Petras Rudys @petrelis
  - Faustas Baltrušaitis @FaustasYe
  - Yeeun Lee @Atay36
  - Chiara Satta @chiarasatta
  - Arnas Navikas @kozahr

- **Server**
  - **Sahak Ivašauskas @sahiva (Sub-Lead)**
  - Taha Abakar Samir @samir737
  
- **Graphics**
  - David Kisel @DavidK14
  - Martynas Jakučionis @Jaku12345

- **Documentation**
  - Sahak Ivašauskas @sahiva

## 3. Mandatory Functionality

One of the key functionalities that our project will consist:

**3.1. HOMEPAGE** 

This is the page that the user sees once he visits the website. 
- At the top, there is the primary button. Clicking it leads you to the main page, which includes the following functionalities:
  - Search bar 
  - Map 
  - Options Bar 
- Under the button, the description of the website is displayed.

**3.2. REGISTRATION WINDOW**

At the top-right of the home page, there are "Login" and "Registration" fields. Clicking the "Log in" button opens the "Log in" window. In that window, the user will have to enter his username or e-mail address in the "Username or e-mail address" field and the password in the "Password" field. That window will also have a button titled "Log in" and a text box as "If you are not registered, register." where "Register" is the text associated with the registration window. After clicking on the main page "Register" button - you'll see a window where you can register, whether you are registering as a seller or a buyer. If you are registering as a seller, a window will appear with the required fields to fill in: 
- Username
- First/Last name
- Phone number (optional as instead, it'll be next to the product) 
- City of residence 
- Address (optional as instead, it'll be next to the product)
- Password 
- Repeat password

If you register as a customer, a window will appear with a required fields to fill in: 
- Username
- City of residence (optional)
- Password 
- Retype password 

Some other information may be added later on to be filled in. Upon registration, **noreply@pingoods.com** will send a message with confirmation to the user.

**3.3. MAP** 

It is located in the centre of the home page on the right side of the search bar. After submitting a search query to the search bar: 
- In the enlarged window, the user sees all the results that best match the search criteria. 
- When zoomed in, the user sees all the products in the area that match the criteria. 
- Clicking on one of the search results will take you to that seller on the map.

**3.4. SEARCH BAR** 

Clicking the primary button on the homepage leads you to the main page with the Search Bar. It'll be located at the top-left of the page. After the search, the search bar will list the most relevant results for the products, and the goods and services tax (PVM) adjusted prices will be displayed. The most suitable product is determined by the combination of your preferred results (vendor's subscription products will be at top), selected categories (product colour), keyword best match, and closest customer distance.

**3.5. OPTIONS BAR**

If the user has logged in to the system, it's located at the top-right of the Main Page. Otherwise, it's not so. When the registered user clicks the button, it'll display for **Vendors**:
- Subscription. Clicking it will display buttons, allowing to: 
  - Buy subscription
  - Check subscription history 
- Edit product posts. Clicking it will display buttons, allowing to:
  -  Edit location 
  -  Edit price
  -  Delete the post
    - Once the remove button is clicked, a confirmation screen will appear in the centre. 
  - Change Phone Number
  - Change City of Living  
  - Change Address 
  - Change Password

If it's clicked by a **Customer**, then he'll get displayed with:
  - History of Purchases 
  - Change Phone Number 
  - Change City of Living 
  - Change Address 
  - Change Password

## 4. Non-Functional Requirements

We, as a team, are expecting that the following non-functional requirements won't cause stress to our users. The software program will have a clear-as sky (not like what we see every day) interface mixed with bright colours! 

**4.1. SECURITY**

Our login and registration system will be as simple as putting on your pants (although sometimes it can be complicated, especially on Monday mornings). and we will implement these security measures for your comfort:
  - Database will only be accessible to administrators.
  - Email and postal address will not be visible in the profile of the customers.
  - The software will detect the existence of two customers with the same ID. (so that you cannot buy from yourself)
  - Age limit to prevent your kids from spending your savings.

**4.2. OPTIMIZATION**

The website may be so optimized that it may even run on a grandmother's cell phone. We guarantee that:
  - The loading time won't exceed 4 seconds, so you will not get bored surfing our webpage. (because who likes to wait more than 4 seconds?)

## 5. Documentation

   The provided information must be referred by the developers in their workflow to prevent disorder and misunderstandings.

   ### 5.1 GitHub formatting

   GitHub formatting [syntaxes](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) should be known for formatting your issue description and commits.

   ### 5.2 Issues

   Issues are created for setting tasks and reporting bugs. All the Issues title must be as follows: "[**TEAMNAME**-**ISSUEID**] **ISSUENAME**", where **TEAMNAME** is the shortcut of the team that must handle this Issue, **ISSUEID** is a unique identification number for each team's Issue, **ISSUENAME** is the short title for the issue. Use uppercase letters appropriately in the title.

   [How We Write GitHub Issues](https://wiredcraft.com/blog/how-we-write-our-github-issues/)

   **5.3 Shortcuts for each team**

   - **Front-End** - **FRNT**
   - **Back-End** - **BACK**
   - **Server** - **SERV**
   - **Graphics** - **GFX**
   - **Documentation** - **DOCS**

   **5.4 Setting Issue fields**

   - **Assignee**: to solve this Issue, assign a specific developer list. Set to null if the problem is not someone's concern, especially
   - **Label**: select the appropriate label for the Issue, including the label of the team to which it is assigned. **If the Issue is a bug**, then **bug** label must be set as well
   - **Projects**: must be set to the team to which the Issue belongs
   - **Milestone**: set the Issue to an appropriate release


   **5.5 Issue Description**

   **If the Issue is a task**, then write a clear, atomic specification of the task. If needed, use visual content, checkboxes, etc.
   
   **If the Issue is a bug**, then shortly describe the problem and write down what is the **Expected result:** and the **Actual result:**.
   
  ### 5.6 Gitflow Workflow

   This [article](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) contains the git-flow model that should be followed when creating, merging, and deleting branches. For naming branches, please refer to the git branch naming [convention](https://deepsource.io/blog/git-branch-naming-conventions/). **Important!: don't use the tracker ID in the branch name as it's provided in the article. We're not going to use it.**

  ### 5.7 Coding conventions

  Each developer has a different coding style, and to avoid confusion, you should follow the Google Style Guide for each programming language.

  -  [**JavaScript**](https://google.github.io/styleguide/jsguide.html)
  -  [**HTML/CSS**](https://google.github.io/styleguide/jsguide.html)
  -  [**Java**](https://google.github.io/styleguide/javaguide.html)
  -  [**PHP**](https://www.php-fig.org/psr/psr-2/)

  

