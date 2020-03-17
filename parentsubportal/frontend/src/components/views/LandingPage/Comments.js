import React, {Component, Fragment} from 'react'
import axios from 'axios'
import PropTypes from "prop-types";
import {Button, Comment, Form, Header} from 'semantic-ui-react'
import {connect} from 'react-redux'
import {postComment} from "../../../actions/comments"
import {getPosts} from "../../../actions/posts";
import './styles.scss'

// TODO: pass posts in ways besides props
export class Comments extends Component {
    constructor(props) {
        super(props)

        this.state = {
            comment: "",
            author: null
        }
    }
    static propTypes = {
        postComment: PropTypes.func.isRequired,
        getPosts: PropTypes.func.isRequired
    };

    onFieldChange(fieldName) {
        return function (event) {
            this.setState({[fieldName]: event.target.value});
        }
    }
    componentDidMount() {
        this.props.getPosts();
        axios
            .get(`/api/auth/user`)
            .then(res => {
                const author = res.data.id
                this.setState({author});
            })
            .catch(err => console.log(err));
    }

    onSubmit(e) {
        e.preventDefault();
        const variables = {
            content: this.state.comment,
            post: this.props.post.id,
            author: this.state.author
        }
        this.props.postComment(variables)
        this.setState({comment: ""});
    }

    render() {
        return (
            <Comment.Group>
                <Header as='h3' dividing>
                    Comments ({this.props.post.total_comments})
                        </Header>
                {/* Comment Lists */}
                {this.props.post.comments.map(comment => (
                    <Comment>
                        <Comment.Avatar src="https://react.semantic-ui.com/images/avatar/small/matt.jpg" />
                        <Comment.Content>
                            <Comment.Author as='a'>Some Name</Comment.Author>
                            <Comment.Metadata><div>Today at 5:42pm</div></Comment.Metadata>
                            <Comment.Text>{comment.content}</Comment.Text>
                            <Comment.Actions>Reply</Comment.Actions>
                        </Comment.Content>
                    </Comment>
                ))}
                <Form reply>
                    <Form.TextArea />
                    <Button content="Add Reply" labelPosition="left" icon="edit" primary />
                </Form>
            </Comment.Group>
        );
    }
}

const mapStateToProps = state => ({
    posts: state.posts.posts
});

export default connect(
    mapStateToProps,
    {postComment, getPosts}
)(Comments);
