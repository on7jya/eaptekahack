import { getCourses } from '../api/index'

export const requestCourses = () => {
    return (dispatch: any) => {
        getCourses()
    }
}

