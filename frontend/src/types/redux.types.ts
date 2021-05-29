export enum ActionTypes {
    REQUEST_DRUGS = '',
    SEND_COURSE = 'SEND_COURSE',
    REQUEST_COURSES = 'REQUEST_COURSES',
    REQUEST_SUBSCRIBE = 'REQUEST_SUBSCRIBE'


}
export interface AnyAction {
    type: string,
    payload: any,
}
export interface MainState {
    drug: string,
    quantity: number,
    schedule: number[],
    startDate: Date,
    frequency: Frequency,
    note: '',
}
export interface Frequency {
    interval: number,
    appropriateTime: string
}






