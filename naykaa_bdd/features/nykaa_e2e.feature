Feature: Nykaa Fragrance End to End Flow

  Scenario: Complete fragrance purchase flow

    Given User opens Nykaa website

    When User searches for "Perfume"

    And User selects first fragrance

    Then Product title should be visible

    When User adds product to cart

    Then Product should be added successfully

    When User opens shopping cart

    Then Shopping cart page should be displayed

    When User views order summary

    And User proceeds to checkout

    Then Order confirmation process should be verified