import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import Cookies from "js-cookie";
import axios from "axios";

function Login({ switchForm, ThemeStyles }) {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const isLoggedInCookie = Cookies.get("isLoggedIn");
    if (isLoggedInCookie === "true") {
      setIsLoggedIn(true);
    }
  }, []);

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: Yup.object({
      email: Yup.string().email("Invalid email address").required("Required"),
      password: Yup.string()
        .min(6, "Must be at least 6 characters")
        .required("Required"),
    }),
    onSubmit: (values, { setSubmitting }) => {
      console.log(values);





      fetch("http://127.0.0.1:5555/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          console.log(data.islogged);
          if (data.islogged) {
            setIsLoggedIn(true);
            Cookies.set("isLoggedIn", true, { expires: 7 });
          }
          setSubmitting(false);
        });
    },
  });

  if (isLoggedIn) {
    return (
      <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "65vh",
      }}
    >
      <div>User is already logged in.</div>
      <button onClick={logout} className="rounded-md bg-green-600 px-3 py-2 text-xl font-semibold text-white shadow-xl hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600">Log out</button>
    </div>
    );


    // Logout function
function logout() {
  fetch("http://127.0.0.1:5555/logout", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => {
      if (res.ok) {
        // Clear the isLoggedIn cookie locally
        Cookies.remove("isLoggedIn");
        // Update the state to reflect that the user is logged out
        setIsLoggedIn(false);
      } else {
        throw new Error("Logout failed");
      }
    })
    .catch((error) => {
      console.error("Logout failed:", error);
    });
}

// Check login status function
function checkLoginStatus() {
  axios.get('http://127.0.0.1:5555/check_login')
      .then(response => {
          if (response.data.islogged === 'loggedin') {
              console.log('Logged in as:', response.data.email);
              // Update UI or redirect to logged-in state
          } else {
              console.log('Not logged in');
              // Update UI or redirect to logged-out state
          }
      })
      .catch(error => {
          console.error('Failed to check login status:', error);
      });
}

  }
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "65vh",
      }}
    >
      <form onSubmit={formik.handleSubmit} className="m-3" style={ThemeStyles}>
        <div className="space-y-12">
          <div className="border-b border-white-950 pb-12">
            <h2 className="text-3xl font-medium py-2 border-white-900 px-4 text-slate-200 leading-30">
              Login Form
            </h2>
            <div className="mt-12 grid grid-cols-0 gap-x-6 gap-y-8 xl:grid-cols-7">
              <div className="xl:col-span-4">
                <label
                  htmlFor="email"
                  className="block text-xl font-medium leading-6"
                >
                  Email address{" "}
                  <span className="text-green-600">(required)</span>
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.email}
                />
                {formik.touched.email && formik.errors.email ? (
                  <div className="text-red-500">{formik.errors.email}</div>
                ) : null}
              </div>
              <div className="xl:col-span-4">
                <label
                  htmlFor="password"
                  className="block text-xl font-medium leading-6"
                >
                  Password <span className="text-green-500">(required)</span>
                </label>
                <input
                  id="password"
                  name="password"
                  type="password"
                  className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.password}
                />
                {formik.touched.password && formik.errors.password ? (
                  <div className="text-red-500">{formik.errors.password}</div>
                ) : null}
              </div>
            </div>
          </div>
        </div>
        <div className="mt-6 flex items-center justify-end gap-x-6">
          <button
            type="submit"
            className="rounded-md bg-green-600 px-3 py-2 text-xl font-semibold text-white shadow-xl hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600"
          >
            Login
          </button>
          <p
            className="register cursor-pointer"
            style={{ cursor: "pointer" }}
            onClick={switchForm}
          >
            Register
          </p>
        </div>
      </form>
    </div>
  );
}

function Register({ switchForm, ThemeStyles }) {
  const formik = useFormik({
    initialValues: {
      firstName: "",
      lastName: "",
      email: "",
      contactNumber: "",
      address: "",
      password: "",
      postalCode: "",
    },
    validationSchema: Yup.object({
      firstName: Yup.string().required("Required"),
      lastName: Yup.string().required("Required"),
      email: Yup.string().email("Invalid email address").required("Required"),
      contactNumber: Yup.string()
        .matches(/^[0-9]+$/, "Must be only digits")
        .min(10, "Must be exactly 10 digits")
        .max(10, "Must be exactly 10 digits")
        .required("Required"),
      address: Yup.string().required("Required"),
      password: Yup.string().required("Required"),
      postalCode: Yup.string().required("Required"),
    }),
    onSubmit: (values, { setSubmitting }) => {
      fetch("http://127.0.0.1:5555/admin", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          setSubmitting(false);
          switchForm()
        });
    },
  });

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "65vh",
      }}
    >
      <form onSubmit={formik.handleSubmit} className="m-3" style={ThemeStyles}>
        <h2 className="pb-12 text-2xl font-medium py-2 border-white-500 px-4 text-slate-200 leading-30">
          Registration Form
        </h2>
        <div className="grid grid-cols-2 gap-8">
          {[
            "firstName",
            "lastName",
            "email",
            "contactNumber",
            "address",
            "password",
            "postalCode",
          ].map((field) => (
            <div key={field}>
              <label htmlFor={field} className="block text-xl font-medium">
                {field.charAt(0).toUpperCase() +
                  field.slice(1).replace(/([A-Z])/g, " $1")}
                <span className="text-green-600">(required)</span>
              </label>
              <input
                id={field}
                name={field}
                type={
                  field === "email"
                    ? "email"
                    : field === "contactNumber"
                    ? "tel"
                    : "text"
                }
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values[field]}
                required
                className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
              />
              {formik.touched[field] && formik.errors[field] ? (
                <div className="text-red-500">{formik.errors[field]}</div>
              ) : null}
            </div>
          ))}
        </div>
        <div className="flex justify-end mt-6">
          <button
            type="submit"
            className="rounded-md bg-green-600 px-3 py-2 text-xl font-semibold text-white shadow-xl hover:bg-green-500"
          >
            Register
          </button>
          <p className="ml-4 cursor-pointer" onClick={switchForm}>
            Login
          </p>
        </div>
      </form>
    </div>
  );
}

function Form() {
  const [isLoginForm, setIsLoginForm] = useState(true);

  const switchForm = () => {
    setIsLoginForm((prev) => !prev);
  };

  return (
    <div>
      {isLoginForm ? (
        <Login switchForm={switchForm} />
      ) : (
        <Register switchForm={switchForm} />
      )}
    </div>
  );
}

export default Form;


