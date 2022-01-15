Overview:
Gemini supports institutional customers as well as retail clients. If institutions are interested in a relationship with Gemini, we encourage them to fill out a registration form and submit it, so that we may contact them. Gemini maintains a sandbox environment which has a copy of this form, and form submissions in the sandbox are ignored, which makes it ideal for testing.

Your task is to write automation that will test not only the typical usage of the form, but negative test cases also. We expect:

that you quantify the number of discrete test cases
that your code is scalable and easy to maintain
that you include clearly-distinguishable positive / ‘Happy Path’ tests and negative tests
that you are prepared to talk through your coding choices, your style and your logic
 
Automation steps:

The automation should start at https://exchange.sandbox.gemini.com/
The automation should click the ‘Create new account’ link
The automation should click the ‘Create a business account’ link, with the resulting page of https://exchange.sandbox.gemini.com/register/institution
The automation should perform happy path and negative testing, demonstrating that the form works with good test data, and prevents users from entering bad data.

These tests should be crafted in a way that allows Developers, other QA Engineers and even Business Analysts an opportunity to read the tests and understand the intent of them.

Using Python is preferred, since it is the primary language used by QA at Gemini, but other languages are acceptable. Using the Selenium WebDriver package is expected. You can use the test framework of your choice (e.g., pytest, unittest, JUnit, etc.), but test data generators and behavior-driven development tools (e.g., Cucumber) should not be used. Other packages may be included, but please detail what should be installed and the method you used to install the packages.

Please submit here:
https://app.greenhouse.io/tests/93709984c50108ebff8aa405332cbec3?utm_medium=email&utm_source=TakeHomeTest
