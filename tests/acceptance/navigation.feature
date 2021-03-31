Feature: Test navigation between pages

  Scenario: Homepage can go to Addon page
    Given User is on Homepage
    When User click "Add-on" item in menu
    Then User is on the "Addon" page

  Scenario: Addon page can go Homepage
    Given User is on "Addon" page
    When User click "Home" item in menu
    Then User is on the Homepage