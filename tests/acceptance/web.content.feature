Feature: Test that page has correct content

#  Scenario: Homepage has correct title
#    Given User is on Homepage
#    Then There is a title shown on the page
#    And The main header is "Summarizing documents"

#  Scenario: Addon page has correct title
#    Given User is on "Addon" page
#    Then There is a title shown on the page
#    And The main header is "Get an overview of every"

#  Scenario: Banner is shown on 'For Business' page
#    Given User is on "ForBusiness" page
#    And User is waiting for the banner to load
#    Then There is a banner shown on the page

  Scenario: User can send contact form
    Given User is on "ContactUs" page
    When User enter "name" in the "Contact.Username" field
    And User enter "mail@test.com" in the "Contact.Email" field
    And User enter "subject" in the "Contact.Subject" field
    And User enter "message" in the "Contact.Comment" field
    And User check agreement
    And User check captcha
    And User press "Submit" button
    Then User is on the success page
#    Then The main header is "Thank you for contacting us!"