import { createStore, applyMiddleware } from 'redux'
import { combineReducers } from 'redux'

import mainReducer from './reducers/main.reducer'

import thunk from 'redux-thunk';

const rootReducer = combineReducers({
    main: mainReducer,
})
const store = createStore(rootReducer, applyMiddleware(thunk))

export type RootState = ReturnType<typeof rootReducer>

export default store;
