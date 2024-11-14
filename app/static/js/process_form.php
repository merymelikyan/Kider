<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    if (!empty($name) && !empty($email) && !empty($message)) {
        // Save to database or send an email
        // Example: save to a file (basic demonstration, adjust for security in real projects)
        $file = 'messages.txt';
        $content = "Name: $name\nEmail: $email\nMessage: $message\n---\n";
        file_put_contents($file, $content, FILE_APPEND);

        echo '<p class="text-success">Thank you! Your message has been received.</p>';
    } else {
        echo '<p class="text-danger">Please fill in all fields.</p>';
    }
} else {
    echo '<p class="text-danger">Invalid request method.</p>';
}
?>
