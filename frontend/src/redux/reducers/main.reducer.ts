import { AnyAction, MainState } from './../../types/redux.types';
import { ActionTypes } from '../../types/redux.types'

const initialState: MainState = {
    drug: 'Viagra',
    quantity: 1,
    schedule: [12.15, 19.00],
    startDate: new Date('12/05/2021'),
    frequency: {
        interval: 1,
        appropriateTime: 'before'
    },
    note: '',
}

export default (state = initialState, { type, payload }: AnyAction) => {
    switch (type) {

        // case ActionTypes.SET_DAY_WEATHER:
        //     return { ...state, forecast: payload }

        default:
            return state
    }
}
export { }