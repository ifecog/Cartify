import React from 'react'
import { Nav, Navbar, Container, NavDropdown } from 'react-bootstrap'
import SearchBox from './SearchBox'

function Header() {
  return (
    <div>
      <header>
        <Navbar bg='dark' variant='dark' expand='lg' collapseOnSelect>
          <Container>
            <Navbar.Brand href='/'>Cartify</Navbar.Brand>
            <Navbar.Toggle aria-controls='basic-navbar-nav' />
            <Navbar.Collapse id='basic-navbar-nav'>
              <Nav className='me-auto'>
                <Nav.Link href='/cart'>
                  <i className='fas fa-shopping-cart' aria-hidden='true'></i>
                  Cart
                </Nav.Link>
                <Nav.Link href='/login'>
                  <i className='fa fa-user' aria-hidden='true'></i>Login
                </Nav.Link>
                {/* <NavDropdown title='Dropdown' id='basic-nav-dropdown'>
                  <NavDropdown.Item href='#action/3.1'>Action</NavDropdown.Item>
                  <NavDropdown.Item href='#action/3.2'>
                    Another action
                  </NavDropdown.Item>
                  <NavDropdown.Item href='#action/3.3'>
                    Something
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href='#action/3.4'>
                    Separated link
                  </NavDropdown.Item>
                </NavDropdown> */}
              </Nav>
            </Navbar.Collapse>
            <div className='ml-auto'>
              <SearchBox />
            </div>
          </Container>
        </Navbar>
      </header>
    </div>
  )
}

export default Header
