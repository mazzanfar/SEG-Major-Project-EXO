import React, { Component, useState } from "react";
import axios from "axios";
import { Button, Form, Message } from "semantic-ui-react";
import { useSelector } from "react-redux";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function VideoForm() {
    const author = useSelector((state) => state.auth.user);
    const topics = useSelector((state) => state.topics.topics);
    const topicOptions = topics.map((topic) => ({
        key: topic.name,
        text: topic.name,
        value: topic.id,
    }));
    const initialState = {
        title: "",
        content: "",
        lower_age: "",
        upper_age: "",
        videoId: "",
        topics: [],
        formSuccess: false,
    };

    const [state, setState] = useState(initialState);

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("title", state.title);
        formData.append("content", state.content);
        formData.append("lower_age", state.lower_age);
        formData.append("upper_age", state.upper_age);
        formData.append("author", author.id);
        formData.append("topics", [state.topics]);
        formData.append("videoId", state.videoId);
        for (var pair of formData.entries()) {
            console.log(pair[0] + ", " + pair[1]);
        }
        axios
            .post("/api/videos/", formData, {
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
            <Form.Input
                required
                label="Lower Age"
                id="lower_age"
                value={state.lower_age}
                onChange={(e, { value }) =>
                    setState({ ...state, lower_age: value })
                }
            />
            <Form.Input
                required
                label="Upper Age"
                id="upper_age"
                value={state.upper_age}
                onChange={(e, { value }) =>
                    setState({ ...state, upper_age: value })
                }
            />
            <Form.Input
                required
                label="Video ID"
                id="videoId"
                onChange={(e, { value }) =>
                    setState({ ...state, videoId: value })
                }
            />
            <Form.Dropdown
                fluid
                multiple
                selection
                placeholder="Topics"
                label="Topics"
                options={topicOptions}
                value={state.topic}
                onChange={(e, { value }) =>
                    setState({ ...state, topics: value })
                }
            />
            <Button>Submit</Button>
            <Message
                success
                header="Video Added Successfuly"
                content="You should see it displayed on the feed page"
            />
        </Form>
    );
}

export default VideoForm;