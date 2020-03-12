import React, {Fragment} from "react";
import Posts from "./Posts";
import Search from "./search/index";
import Form from "./Form";
import './styles.scss'

export default function LandingPage() {
    return (
        <Fragment>
            <div class="d-flex" id="wrapper">
                <div class="bg-light border-right" id="sidebar-wrapper">
                    <div class="list-group list-group-flush">
                        <a href="#" class="list-group-item list-group-item-action bg-light">Documents</a>
                        <a href="#" class="list-group-item list-group-item-action bg-light">Blogs</a>
                        <a href="#" class="list-group-item list-group-item-action bg-light">Topics</a>
                        <a href="#" class="list-group-item list-group-item-action bg-light">Grooups</a>
                    </div>
                </div>
                <div id="page-content-wrapper">
                    <Search />
                    <Posts />
                    <Form />
                </div>
            </div>
        </Fragment>
    );
}
