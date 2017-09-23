# Node Red Create New Node Notes

Về cơ bản, một Node trong Node Red bao gồm 3 thành phần chính tương ứng với 3 file mà chúng ta cần tạo ra: file ```package.json``` khai báo cho Node Red biết node đang xét là một ```node module```, một file js định nghĩa các  công việc mà node đang tạo ra sẽ làm, và một file html định nghĩa giao diện của node trên node red dashboard, cũng như giao diện cho phép cấu hình các thuộc tính của node. Tất cả các file này cần được đặt trong cùng một thư mục.

## File package.json

Trong file package.json, chúng ta cần chú ý tới các thành phần sau:

## File html

file HTMl của một node trong Node Red cần có các phần cơ bản sau:

### Phần định nghĩa giao diện hiển thị

### Phần đăng ký với giao diện dashboard giao diện của node mới

Phần này chứa toàn bộ các thông tin mà dashboard cần để xử lý hiển thị giao diện cho node mới của chúng ta.

```javascript
<script type="text/javascript">
    RED.nodes.registerType('node-name',{
        // node definition
    });
</script>
```

node-name là tên định danh của node với node red, và nó phải trùng với giá trị node-name được đăng ký ở file js

Phần **node definition** định nghĩa các thuộc tính của node, bao gồm:

- category: (string) the palette category the node appears in
- defaults: (object) the editable properties for the node.
- credentials: (object) the credential properties for the node.
- inputs: (number) how many inputs the node has, either 0 or 1.
- outputs: (number) how many outputs the node has. Can be 0 or more.
- color: (string) the background colour to use.
- label: (string|function) the label to use in the workspace.
- labelStyle: (string|function) the style to apply to the label.
- inputLabels: (string|function) optional label to add on hover to the input port of a node.
- outputLabels: (string|function) optional labels to add on hover to the output ports of a node.
- icon: (string) the icon to use.
- align: (string) the alignment of the icon and label.
- oneditprepare: (function) called when the edit dialog is being built. See custom edit behaviour.
- oneditsave: (function) called when the edit dialog is okayed. See custom edit behaviour.
- oneditcancel: (function) called when the edit dialog is cancelled. See custom edit behaviour.
- oneditdelete: (function) called when the delete button in a configuration node’s edit dialog is pressed. See custom edit behaviour.
- oneditresize: (function) called when the edit dialog is resized. See custom edit behaviour.
- onpaletteadd: (function) called when the node type is added to the palette.
- onpaletteremove: (function) called when the node type is removed from the palette.
