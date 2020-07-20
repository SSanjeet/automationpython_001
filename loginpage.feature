Feature: Login Page

  Scenario: Verify testing world page
    Given User enter the url
    When User enter the username "sanjeet" and password "test123"
    And User  lick on the login button
    Then User verify the My Profile page should display