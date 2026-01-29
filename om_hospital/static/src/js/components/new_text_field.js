/** @odoo-module **/
import {registry} from "@web/core/registry";
// import { Component, useState } from "@odoo/owl";
const {Component,useState} = owl;

export class NewField extends Component{
    // setup(){
    //     this.state = useState({value:1})
    // }

    }
NewField.template = 'om_hospital.TodoList'

registry.category("actions").add("om_hospital.todo_list",NewField)