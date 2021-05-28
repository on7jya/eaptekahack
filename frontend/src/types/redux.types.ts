export enum ActionTypes {
    TEST = 'TEST',

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






