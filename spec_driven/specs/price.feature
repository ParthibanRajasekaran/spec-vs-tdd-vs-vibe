Feature: Checkout price
  Scenario: VAT then discount
    Given a base amount of 100
    And VAT is 20 percent
    When I apply the code "WELCOME10"
    Then the final price should be 108.0

