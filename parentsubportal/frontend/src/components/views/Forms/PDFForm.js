import React, { Component, useState } from "react";
import axios from "axios";
import { Button, Form, Message } from "semantic-ui-react";
import { useSelector } from "react-redux";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function PDFForm() {
    const author = useSelector((state) => state.auth.user);
    const topics = useSelector((state) => state.topics.topics);
    const disabilities = useSelector(
        (state) => state.disabilities.disabilities
    );

    const topicOptions = topics.map((topic) => ({
        key: topic.name,
        text: topic.name,
        value: topic.id,
    }));

    const disabilityOptions = disabilities.map((disability) => ({
        key: disability.name,
        text: disability.name,
        value: disability.id,
    }));

    const initialState = {
        title: "",
        content: "",
        age_group: "",
        topics: [],
        disabilities: [],
        pdf_file: "",
        formSuccess: false,
    };

    // TODO: Get age groups from backend rather than hardcode
    const ageGroupOptions = [
        { key: "0-4", value: "0-4", text: "0-4" },
        { key: "4-11", value: "4-11", text: "4-11" },
        { key: "11-18", value: "11-18", text: "11-18" },
        { key: "18-25", value: "18-25", text: "18-25" },
        { key: "N/A", value: "N/A", text: "N/A" },
    ];

    const [state, setState] = useState(initialState);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(state);
        const formData = new FormData();
        formData.append("title", state.title);
        formData.append("content", state.content);
        formData.append("age_group", state.age_group);
        formData.append("author", author.id);
        state.topics.forEach((item) => {
            formData.append("topics", item);
        });
        state.disabilities.forEach((item) => {
            formData.append("disabilities", item);
        });
        formData.append("pdf_file", state.pdf_file);
        axios
            .post("/api/pdfs/", formData, {
                headers: {
                    "content-type": "multipart/form-data",
                },
            })
            .then((res) => {
                console.log(res);
            })
            .catch((err) => console.log(err.response.data));
        setState({ ...state, formSuccess: true });
    };

    return (
        <Form onSubmit={handleSubmit} success={state.formSuccess}>
            <Form.Input
                required
                label="Title"
                id="title"
                value={state.title}
                onChange={(e, { value }) =>
                    setState({ ...state, title: value })
                }
            />
            <Form.Input
                required
                label="Content"
                id="content"
                value={state.content}
                onChange={(e, { value }) =>
                    setState({ ...state, content: value })
                }
            />
            <Form.Dropdown
                fluid
                placeholder="Age Group"
                label="Age Group"
                options={ageGroupOptions}
                value={state.age_group}
                onChange={(e, { value }) =>
                    setState({ ...state, age_group: value })
                }
            />
            <Form.Dropdown
                inlineStyle={{
                    overflow: "initial",
                }}
                fluid
                required
                multiple
                selection
                placeholder="Topics"
                label="Topics"
                options={topicOptions}
                value={state.topics}
                onChange={(e, { value }) =>
                    setState({ ...state, topics: value })
                }
            />
            <Form.Dropdown
                inlineStyle={{
                    overflow: "initial",
                }}
                fluid
                multiple
                selection
                placeholder="Disabilities"
                label="Disabilities"
                options={disabilityOptions}
                value={state.disabilities}
                onChange={(e, { value }) =>
                    setState({ ...state, disabilities: value })
                }
            />
            <Form.Input
                required
                type="file"
                accept="pdf"
                label="PDF file"
                onChange={(e, { value }) =>
                    setState({ ...state, pdf_file: e.target.files[0] })
                }
            />
            <Button>Submit</Button>
            <Message
                success
                header="PDF Added Successfuly"
                content="You should see it displayed on the feed page"
            />
        </Form>
    );
}

export default PDFForm;
