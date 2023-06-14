import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { Form, Button, Row, Col, Table } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'
import Loader from '../components/Loader'
import { getUserDetails } from '../actions/userActions'

function ProfileScreen() {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [message, setMessage] = useState('')

  const navigate = useNavigate()
  const dispatch = useDispatch()

  const userDetails = useSelector((state) => state.userDetails)
  const { error, loading, user } = userDetails

  const userLogin = useSelector((state) => state.userLogin)
  const { userInfo } = userLogin

  useEffect(() => {
    if (!userInfo) {
      navigate('/login')
    } else {
      if (!user || !user.name || userInfo._id !== user._id) {
        dispatch(getUserDetails('profile'))
      } else {
        setFirstName(user.first_name)
        setLastName(user.last_name)
        setEmail(user.email)
      }
    }
  }, [navigate, userInfo, user, dispatch])

  const submitHandler = (e) => {
    e.preventDefault()

    if (password !== confirmPassword) {
      setMessage('Passwords do not match')
    } else {
      console.log('hey!')
    }
  }

  return (
    <Row>
      <Col md={3}>
        <h2>User Profile</h2>

        {message && <Message variant='danger'>{message}</Message>}
        {error && <Message variant='danger'>{error}</Message>}
        {loading && <Loader />}
        <Form onSubmit={submitHandler}>
          <Form.Group controlId='firstName' className='py-3'>
            <Form.Label>First Name</Form.Label>
            <Form.Control
              required
              type='name'
              placeholder='first name'
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId='lastName' className='py-3'>
            <Form.Label>Last Name</Form.Label>
            <Form.Control
              required
              type='name'
              placeholder='last name'
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId='email' className='py-3'>
            <Form.Label>Email</Form.Label>
            <Form.Control
              required
              type='email'
              placeholder='email'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId='password' className='py-3'>
            <Form.Label>Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='password (reset?)'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId='passwordConfirm' className='py-3'>
            <Form.Label> Confirm Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='confirm password'
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Button type='submit' variant='primary'>
            Update
          </Button>
        </Form>
      </Col>
    </Row>
  )
}

export default ProfileScreen