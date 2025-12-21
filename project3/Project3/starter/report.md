Student’s Name: Fatima Nadeem  
Professor’s Name: [Professor Name]  
Class Number: ET 721  
Date: December 21, 2025  

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Before adding unit tests to the Flask application, the overall test coverage was very low. Only a small portion of the application logic was being tested, which made it difficult to confidently modify or extend the code. Many functions and database interactions were untested, increasing the risk of runtime errors and unexpected failures. At this stage, even small changes could cause bugs without being immediately detected.

After implementing unit tests using pytest, the test coverage significantly improved. By writing tests for the data models and validating required fields, the project achieved a much higher level of confidence in its core functionality. The final test coverage reached a strong level suitable for a production-ready application. In total, multiple unit tests were added to validate model creation, database constraints, and application behavior.

## Untested Code: Effects

Before tests were written, it was difficult to fully understand all features and edge cases of the codebase. Without tests, verifying correctness required manually running the application and testing each endpoint by hand, which was time-consuming and error-prone. For example, missing required database fields caused runtime errors that were not obvious until execution. Testing the API manually also increased the chance of overlooking edge cases.

Manually testing the API required setting up the server, sending requests, and checking responses, which made development slower and less reliable. This highlighted the importance of automated testing in modern software development.

## Benefits of Unit and API Testing

Unit and API testing greatly improved the stability and reliability of the application. Unit tests ensured that individual components, such as database models, behaved as expected. API tests verified that endpoints returned correct responses and handled invalid input properly. Together, these tests made it easier to detect bugs early in the development process.

Testing also made the code easier to understand. Reading test cases helped clarify how functions and models were intended to be used, making future development more efficient.

## Role of Continuous Integration (CI)

Continuous Integration (CI) plays a crucial role in maintaining software quality. By automatically running tests whenever code is pushed to GitHub, CI ensures that new changes do not break existing functionality. This automated feedback loop reduces deployment risks and increases confidence among developers and stakeholders. CI encourages best practices and helps maintain long-term project stability.

## Future Improvements

In the future, additional tests can be added to cover more API endpoints and edge cases. Increasing code coverage further and integrating coverage reports into CI workflows would continue improving code quality. Expanding tests to include performance and integration testing would also strengthen the application as it scales.
