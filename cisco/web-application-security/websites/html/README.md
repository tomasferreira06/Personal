# HTML

## What is HTML?

HyperText Markup Language (HTML) is the language websites are written in.&#x20;

### Elements

Elements (also known as tags) are the building blocks of HTML pages and tells the browser how to display content.&#x20;

**The code below shows a simple HTML document, the structure of which is the same for every website:**

<figure><img src="../../../../.gitbook/assets/Capture (32).PNG" alt=""><figcaption></figcaption></figure>

* The <mark style="color:blue;">`<!DOCTYPE html>`</mark> defines that the page is a HTML5 document. This helps with standardisation across different browsers and tells the browser to use HTML5 to interpret the page.
* The <mark style="color:blue;">`<html>`</mark> element is the root element of the HTML page - all other elements come after this element.
* The <mark style="color:blue;">`<head>`</mark> element contains information about the page (such as the page title)
* The <mark style="color:blue;">`<body>`</mark> element defines the HTML document's body; only content inside of the body is shown in the browser.
* The <mark style="color:blue;">`<h1>`</mark> element defines a large heading
* The <mark style="color:blue;">`<p>`</mark> element defines a paragraph
* There are many other elements (tags) used for different purposes. For example, there are tags for buttons (<mark style="color:blue;">`<button>`</mark>), images (<mark style="color:blue;">`<img>`</mark>), lists, and much more.&#x20;



Tags can contain attributes such as the class attribute which can be used to style an element (e.g. make the tag a different color) <mark style="color:blue;">`<p class="bold-text">`</mark>, or the _<mark style="color:yellow;">src</mark>_ attribute which is used on images to specify the location of an image: <mark style="color:blue;">`<img src="img/cat.jpg">`</mark>`.`

An element can have multiple attributes each with its own unique purpose, e.g., <mark style="color:blue;">\<p attribute1="value1" attribute2="value2"></mark>.

Elements can also have an id attribute (<mark style="color:blue;">`<p id="example">`</mark>), which is unique to the element. Unlike the class attribute, where multiple elements can use the same class, an element must have different id's to identify them uniquely.&#x20;

Element id's are used for styling and to identify it by JavaScript.







\
