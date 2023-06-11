import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams, useNavigate } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'
import Rating from '../components/Rating'
import Loader from '../components/Loader'
import Message from '../components/Message'
import { listProductDetails } from '../actions/productActions'

function ProductScreen() {
  const { id } = useParams()
  const dispatch = useDispatch()

  const productDetails = useSelector((state) => state.productDetails)
  const { error, loading, product } = productDetails

  useEffect(() => {
    dispatch(listProductDetails(id))
  }, [id, dispatch])

  const navigate = useNavigate()

  return (
    <div>
      <Link to='/' className='btn btn-light' my-3>
        Go Back
      </Link>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message>{error}</Message>
      ) : (
        <div>
          <Row>
            <Col md={6}>
              <Image src={product.image} alt={product.name} fluid />
            </Col>

            <Col md={3}>
              <ListGroup variant='flush'>
                <ListGroup.Item className='list-group-item-no-decoration'>
                  <h3>{product.name}</h3>
                </ListGroup.Item>

                <ListGroup.Item>Price: ${product.price}</ListGroup.Item>

                <ListGroup.Item>
                  Quantity: {product.count_in_stock}
                </ListGroup.Item>

                <ListGroup.Item>
                  Description: {product.description}
                </ListGroup.Item>

                <ListGroup.Item>
                  <Rating
                    value={product.rating}
                    text={`${product.num_of_reviews} reviews`}
                    color={'#f8e825'}
                  />
                </ListGroup.Item>
              </ListGroup>
            </Col>
          </Row>
        </div>
      )}
    </div>
  )
}

export default ProductScreen
