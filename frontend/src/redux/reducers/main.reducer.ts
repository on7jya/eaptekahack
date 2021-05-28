import { anyAction } from './../../types/redux.types';
import { ActionTypes } from '../../types/redux.types'

const initialState = {
    test: null,
}

export default (state = initialState, { type, payload }: anyAction) => {
    switch (type) {

        // case ActionTypes.SET_DAY_WEATHER:
        //     return { ...state, forecast: payload }

        default:
            return state
    }
}
export { }