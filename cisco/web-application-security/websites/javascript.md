# JavaScript

JavaScript (JS) is one of the most popular coding languages in the world and allows pages to become interactive.&#x20;

HTML is used to create the website structure and content, while JavaScript is used to control the functionality of web pages - without JavaScript, a page would not have interactive elements and would always be static.

&#x20;JS can dynamically update the page in real-time, giving functionality to change the style of a button when a particular event on the page occurs (such as when a user clicks a button) or to display moving animations.

<mark style="color:red;">JavaScript is added within the page source code and can be either loaded within</mark> <mark style="color:blue;">`<script>`</mark> <mark style="color:red;">tags or can be included remotely with the</mark> _<mark style="color:yellow;">src</mark>_ <mark style="color:red;">attribute:</mark>&#x20;

<mark style="color:blue;">`<script src="/location/of/javascript_file.js"></script`</mark>

<mark style="color:red;">The following JavaScript code finds a HTML element on the page with the id of "demo" and changes the element's contents to "Hack the Planet" :</mark>&#x20;

<mark style="color:blue;">`document.getElementById("demo").innerHTML = "Hack the Planet";`</mark>

HTML elements can also have events, such as "onclick" or "onhover" that execute JavaScript when the event occurs.

&#x20;<mark style="color:red;">The following code changes the text of the element with the demo ID to Button Clicked:</mark>&#x20;

<mark style="color:blue;">`<button onclick='document.getElementById("demo").innerHTML = "Button Clicked";'>Click Me!</button>`</mark>&#x20;

Onclick events can also be defined inside the JavaScript script tags, and not on elements directly.&#x20;

