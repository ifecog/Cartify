import axios from 'axios'
import { CART_ADD_ITEM, CART_REMOVE_ITEM } from '../constants/cartConstants'

export const addToCart = (id, qty) => async (dispatch, getState) => {
  const { data } = await axios.get(`/api/products/${id}`)

  dispatch({
    type: CART_ADD_ITEM,
    payload: {
      product: data._id,
      name: data.name,
      image: data.image,
      price: data.price,
      count_in_stock: data.count_in_stock,
      qty,
    },
  })

  localStorage.setItem('cartItems', JSON.stringify(getState().cart.cartItems))
}

export const addToCar = (id, qty) => (dispatch, getState) => {
  axios
    .get(`/api/products/${id}`)
    .then((response) => {
      const { _id, name, image, price, count_in_stock } = response.data
      dispatch({
        type: CART_ADD_ITEM,
        payload: {
          product: _id,
          name,
          image,
          price,
          count_in_stock,
          qty,
        },
      })
      localStorage.setItem(
        'cartItems',
        JSON.stringify(getState().cart.cartItems)
      )
    })
    .catch((error) => console.log(error))
}

export const RemoveFromCart = (id, qty) => (dispatch, getState) => {
  dispatch({
    type: CART_REMOVE_ITEM,
    payload: id,
  })
}
