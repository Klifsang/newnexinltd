import { useEffect, useState } from "react";
import * as Yup from "yup";
import axios from "axios";
import { useFormik } from 'formik';


function TaskForm({ switchForm, ThemeStyles }) {
  const formik = useFormik({
    initialValues: {
      Subject: '',
      Description: '',
      deadline: '',
    },
    validationSchema: Yup.object({
      Subject: Yup.string().required('Required'),
      Description: Yup.string().required('Required'),
      deadline: Yup.string().required('Required'),
    }),
    onSubmit: (values, { setSubmitting }) => {
      console.log(values);

      (async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5555/tickets', values);
            console.log(response.data.message);

        } catch (error) {
            console.log(error.response.data.message);
        }
    })();
    
    },
  });

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '65vh' }}>
      <form onSubmit={formik.handleSubmit} className="m-5" style={{ ...ThemeStyles, width: '80%' }}>
        <h2 className="pb-12 text-2xl font-medium py-2 border-white-500 px-4 text-slate-200 leading-30">Task Entry Form</h2>
        <div className="grid gap-8">
          {["Subject", "Description", "deadline"].map(field => (
            <div key={field}>
              <label htmlFor={field} className="block text-xl font-medium">
                {field.charAt(0).toUpperCase() + field.slice(1).replace(/([A-Z])/g, ' $1')}<span className="text-green-600">(required)</span>
              </label>
              {field === "Description" ? (
                <textarea
                  id={field}
                  name={field}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values[field]}
                  required
                  className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
                />
              ) : field === "deadline" ? (
                <input
                  id={field}
                  name={field}
                  type="datetime-local"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values[field]}
                  required
                  className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
                />
              ) : (
                <input
                  id={field}
                  name={field}
                  type="text"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values[field]}
                  required
                  className="mt-1 block w-full px-3 py-2 bg-teal-750 border border-gray-300 rounded-md shadow-xl focus:outline-none focus:ring-orange-900 focus:border-orange-900"
                />
              )}
              {formik.touched[field] && formik.errors[field] ? <div className="text-red-500">{formik.errors[field]}</div> : null}
            </div>
          ))}
        </div>
        <div className="flex justify-end mt-6">
          <button type="submit" className="rounded-md bg-green-600 px-3 py-2 text-xl font-semibold text-white shadow-xl hover:bg-green-500">Submit</button>
        </div>
      </form>
    </div>
  );
}

export default TaskForm;
