Feature: Test that page has correct content

  Scenario: Homepage has correct title
    Given User is on Homepage
    Then There is a title shown on the page
#    And The title is "Summarizing documents"

  Scenario: Addon page has correct title
    Given User is on "Addon" page
    Then There is a title shown on the page
#    And The title is "Get an overview of every"

  Scenario: Banner is shown on 'For Business' page
    Given User is on "ForBusiness" page
    And User is waiting for the banner to load
    Then There is a banner shown on the page