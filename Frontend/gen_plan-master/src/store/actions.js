import axios from '../axios.js'
import router from '../router/index.js'


export const login = ({
    commit
}, object) => {
    console.log(object.email, object.password)
    axios
        .post("api/auth/signin/", {
            password: object.password,
            email: object.email
        })
        .then(async (response) => {
            window.localStorage.setItem('token', response.data.accessToken)
            window.localStorage.setItem('UserId', response.data.userId)
            commit("SET_TOKEN", response.data.accessToken)
            commit("SET_USERID", response.data.userId)
            commit("LOGIN_SUCCESS", true)
            router.push("/");
            console.log(response.data)
        })
        .catch(function (error) {
            commit("LOGIN_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("LOGIN_ERROR", error.response.data.message)
            } else {
                commit("LOGIN_ERROR", error.response.data.message)
            }
        });
}

export const register = ({
    commit
}, object) => {
    console.log(object.email,object.username, object.password)
    axios
        .post("api/auth/signup/", {
            email: object.email,
            username: object.username,
            password: object.password,
        })
        .then(async () => {
            commit("REGISTER_SUCCESS", true)
            router.push("/register/verify");
        })
        .catch(function (error) {
            commit("REGISTER_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("REGISTER_ERROR", error.response.data.message)
            } else {
                commit("REGISTER_ERROR", error.response.data.message)
            }
        });
}



export const verifyEmail = ({
    commit
}, object) => {
    console.log(object.email, object.token)
    axios
        .post("api/auth/verifyEmail/", {
            email: object.email,
            token: object.token,
        })
        .then(async () => {
            commit("REGISTER_VERIFY_SUCCESS", true)
            router.push("/login");
        })
        .catch(function (error) {
            commit("REGISTER_VERIFY_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("REGISTER_VERIFY_ERROR", error.response.data.message)
            } else {
                commit("REGISTER_VERIFY_ERROR", error.response.data.message)
            }
        });
}

export const resendToken = ({
    commit
}, object) => {
    console.log(object.email)
    axios
        .post("api/auth/resendEmailToken/", {
            email: object.email,
        })
        .then(function (response) {
            console.log(response);
            commit("RESEND_TOKEN_SUCCESS", true)
        })
        .catch(function (error) {
            commit("RESEND_TOKEN_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("RESEND_TOKEN_ERROR", error.response.data.message)
            } else {
                commit("RESEND_TOKEN_ERROR", error.response.data.message)
            }
        });
}

export const recoverPassword = ({
    commit
}, object) => {
    console.log(object.email)
    axios
        .post("api/auth/recoverPassword/", {
            email: object.email,
        })
        .then(function (response) {
            console.log(response);
            commit("SEND_PIN_SUCCESS", true)
            router.push("/new/password");
        })
        .catch(function (error) {
            commit("SEND_PIN_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("SEND_PIN_ERROR", error.response.data.message)
            } else {
                commit("SEND_PIN_ERROR", error.response.data.message)
            }
        });
}

export const resetPassword = ({
    commit
}, object) => {
    console.log(object.token, object.password)
    axios
        .post("api/auth/resetPassword/", {
            token: object.token,
            password: object.password
        })
        .then(function (response) {
            console.log(response);
            commit("NEW_PASS_SUCCESS", true)
            router.push("/login");
        })
        .catch(function (error) {
            commit("NEW_PASS_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("NEW_PASS_ERROR", error.response.data.message)
            } else {
                commit("NEW_PASS_ERROR", error.response.data.message)
            }
        });
}

export const fetchSubjects = ({
    commit
},object) => {
    axios.get("api/get/all/subjects",{ headers: { 'x-access-token': `${object.token}`}})
        .then((response) => {
            console.log(response)
            commit("SET_SUBJECTS", response.data)
        })
        .catch((err) => console.log(err));
}

export const sendSubject = ({
    commit
}, object) => {
    console.log(object.token, object.subject_name)
    axios
        .post("api/add/subject", {
            token: object.token,
            subject_name: object.subject_name
        })
        .then(function (response) {
            console.log(response);
            commit("ADD_SUBJECT_SUCCESS", true)
            router.go();
        })
        .catch(function (error) {
            commit("ADD_SUBJECT_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("ADD_SUBJECT_ERROR", error.response.data.message)
            } else {
                commit("ADD_SUBJECT_ERROR", error.response.data.message)
            }
        });
}

export const fetchTeachers = ({
    commit
},object) => {
    axios.get("api/get/all/teachers",{ headers: { 'x-access-token': `${object.token}`}})
        .then((response) => {
            console.log(response)
            commit("SET_TEACHERS", response.data)
        })
        .catch((err) => console.log(err));
}

export const sendTeacher = ({
    commit
}, object) => {
    console.log(object.token, object.name, object.surname, object.email, object.list_of_subjects)
    axios
        .post("api/add/teacher", {
            token: object.token,
            name: object.name,
            surname: object.surname,
            email: object.email,
            list_of_subjects: object.list_of_subjects
        })
        .then(function (response) {
            console.log(response);
            commit("ADD_TEACHER_SUCCESS", true)
            router.go();
        })
        .catch(function (error) {
            commit("ADD_TEACHER_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("ADD_TEACHER_ERROR", error.response.data.message)
            } else {
                commit("ADD_TEACHER_ERROR", error.response.data.message)
            }
        });
}

export const fetchClassrooms = ({
    commit
},object) => {
    axios.get("api/get/all/classrooms",{ headers: { 'x-access-token': `${object.token}`}})
        .then((response) => {
            console.log(response)
            commit("SET_CLASSROOMS", response.data)
        })
        .catch((err) => console.log(err));
}

export const sendClassroom = ({
    commit
}, object) => {
    console.log(object.token, object.name, object.list_of_subjects)
    axios
        .post("api/add/classroom", {
            token: object.token,
            name: object.name,
            list_of_subjects: object.list_of_subjects
        })
        .then(function (response) {
            console.log(response);
            commit("ADD_CLASSROOM_SUCCESS", true)
            router.go();
        })
        .catch(function (error) {
            commit("ADD_CLASSROOM_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("ADD_CLASSROOM_ERROR", error.response.data.message)
            } else {
                commit("ADD_CLASSROOM_ERROR", error.response.data.message)
            }
        });
}

export const fetchClasses = ({
    commit
},object) => {
    axios.get("api/get/all/classes",{ headers: { 'x-access-token': `${object.token}`}})
        .then((response) => {
            console.log(response)
            commit("SET_CLASSES", response.data)
        })
        .catch((err) => console.log(err));
}

export const sendClass = ({
    commit
}, object) => {
    console.log(object.token, object.name, object.list_of_lessons)
    axios
        .post("api/add/class", {
            token: object.token,
            name: object.name,
            list_of_lessons: object.list_of_subjects
        })
        .then(function (response) {
            console.log(response);
            commit("ADD_CLASSES_SUCCESS", true)
            router.go();
        })
        .catch(function (error) {
            commit("ADD_CLASSES_SUCCESS", false)
            if (error.response.data.message === "Validation error") {
                commit("ADD_CLASSES_ERROR", error.response.data.message)
            } else {
                commit("ADD_CLASSES_ERROR", error.response.data.message)
            }
        });
}