import React, { Component } from 'react';
import axios from 'axios';
import { Button, Form, Message } from 'semantic-ui-react'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default class PDFForm extends Component {
    state = {
        title: '',
        content: '',
        lower_age: '',
        upper_age: '',
        author: 15,
        pdf_file: null,
        formSuccess: false
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("title", this.state.title);
        formData.append("content", this.state.content);
        formData.append("lower_age", this.state.lower_age);
        formData.append("upper_age", this.state.upper_age);
        formData.append("author", 15);
        formData.append("pdf_file", this.state.pdf_file);
        axios
        .post('/api/pdfs/', formData, {
            headers: {
                'content-type': 'multipart/form-data'
            }
        })
        .then(res => {
            console.log("hi")
            console.log(res)
        }).catch(err => console.log(err.response.data));
        this.setState({formSuccess:true});
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    };

    handleFileChange = (e) => {
        this.setState({
            pdf_file: e.target.files[0]
        })
    };

    render() {
        return (
            <Form onSubmit={this.handleSubmit} success={this.state.formSuccess}>
                <Form.Input required label="Title" id="title" value={this.state.title} onChange={this.handleChange}/>
                <Form.Input required label="Content" id="content" value={this.state.content} onChange={this.handleChange}/>
                <Form.Input required label="Lower Age" id="lower_age" value={this.state.lower_age} onChange={this.handleChange}/>
                <Form.Input required label="Upper Age" id="upper_age" value={this.state.upper_age} onChange={this.handleChange}/>
                <Form.Input required type="file" accept="pdf" label="Content" onChange={this.handleFileChange}/>
                <Button>Submit</Button>
                <Message
                success
                header="PDF Added Successfuly"
                content="You should see it displayed on the feed page"
                />
            </Form>
        );
    }
}
