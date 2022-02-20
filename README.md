# Helphone-IVRS
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) </br>

Helpline for those without Smartphone

Helphone is an IVRS based solution designed to help elders and others without a smartphone.

It is designed primarily for those who can't use services like Swiggy, Zomato, Pharmeasy and Big Basket to get their required supplies due to either non availability of smartphone or not knowing how to use such apps.

Based on our survey, many senior citizens from both rural and urban areas and many of the adults from urban areas weren't comfortable in using the above mentioned services and so, We thought of simplifying the process.

And here in front of you, is the solution.

Helphone simplifies the above mentioned issue by connecting the user straight to the vendor. All the user would have to do is to call the Helpline and then the following happens.

1. Helphone asks for the preferred Language (```Tamil``` or ```English``` or ```Hindi```)
2. The user selects the required language
3. Helphone asks for the required service (```Groceries``` or ```Dairy Needs``` or ```Medical Emergency``` or ```Pharmacy Needs```)
4. The user selects the required service.
5. Helphone connects them with the nearest service provider.

## Technologies used

Django </br>
Ngrok [Port forwarding for testing] </br>
Twilio Number </br>
Twilio Webhooks </br>
Twilio Voice API </br>

## Demo Video

https://user-images.githubusercontent.com/74530357/154845436-9ad4b5bf-40a6-4848-923a-3fd98d85dd97.mp4

## Installation and Set up

To test ```Helphone```, first clone this repository.

Open a new terminal window.
```
git clone https://github.com/srivathsanvenkateswaran/Helphone-IVRS
```
move into the directory
```
cd Helphone-IVRS
```
Now follow the video to set up ```Helphone```.

https://user-images.githubusercontent.com/74530357/154845493-4fd13666-d473-4cb0-8496-82a5be738b3a.mp4

## Post deployment

Once you've deployed the ```Helphone``` app, make sure you create a Twilio Account and get a Twilio Phone Number.

You've to connect the app with the number using webhooks so create the helpline. 

## Note

I've not set it up ```Helphone``` publicly due to non availability of server. Feel free to test ```Helphone``` in your local environment. If you liked ```Helphone``` you are free to set it up in your own server.

Feel free to contact me in case of any doubt.
