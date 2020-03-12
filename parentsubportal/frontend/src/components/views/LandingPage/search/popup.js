import React from "react";
import { AgeSlider } from './AgeSlider'

export default class Popup extends React.Component {
    constructor(props) {
    super(props);
    }

    render() {
        const { topics, posts, documents, isOpen } = this.props;
        // Do not show popup
        if (!isOpen) return null;
        return (
            <div className="spopup">
                <div className="container">
                    <div className="content">
                        <div class="row">
                            <div class="col-md-6">
                                {topics &&
                                    topics.map((topic, idx) => {
                                        return (
                                            <div className="item" key= {idx}>
                                                Topic: {topic.name}
                                            </div>
                                        );
                                    })}
                                {posts &&
                                    posts.map((post, idx) => {
                                        return (
                                            <div className="item" key= {idx}>
                                                Post: {post.title}
                                            </div>
                                        );
                                    })}
                                {documents &&
                                    documents.map((doc, idx) => {
                                        return (
                                            <div className="item" key= {idx}>
                                                Document: {doc.title}
                                            </div>
                                        );
                                    })}
                                {!topics && !posts && <div className="warning">Nothing Found!</div>}
                            </div>
                            <div class="col-md-6">
                                <AgeSlider/>
                            </div>
                            </div>
                        </div>
                        <div className="footer">Type keyword to search for conditions</div>
                    </div>
                </div>
        );
    }
}
