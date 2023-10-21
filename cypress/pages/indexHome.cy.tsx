import React from 'react'
import Home from './index'



describe('<Home />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<Home />)
    cy.get('[data-cy=docs-link]').should('be.visible')
    cy.get('[data-cy=click-link]').click()
    //click on the link
    //cy.get('.cyclick').click()
  })
})