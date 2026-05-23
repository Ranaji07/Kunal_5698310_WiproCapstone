Feature: Nykaa Fragrance Validation

  Scenario Outline: Positive Product Search Validation

    Given User opens Nykaa website
    When User searches fragrance product "<product>"
    Then Search results should appear

    Examples:
      | product |
      | Perfume |
      | Dior    |
      | Gucci   |
      | Cologne |


  Scenario Outline: Negative Product Search Validation

    Given User opens Nykaa website
    When User searches fragrance product "<product>"
    Then Invalid search message should appear

    Examples:
      | product        |
      | @@@@@@@        |
      | invalidproduct |