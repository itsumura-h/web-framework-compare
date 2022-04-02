<main>
    <section>
      @if($isLogin)
        <form method="POST" action="/signout">
          <header>
            <h2>You are logged in!</h2>
            <p>Login Email: {{ $email }}</p>
          </header>
          @csrf
          <button type="submit">Sign out</button>
        </form>
      @else
        <form method="POST" action="/">
          @csrf
          <p>
            <input type="text" name="email" placeholder="email">
          </p>
          <p>
            <input type="password" name="password" placeholder="password">
          </p>
          <button type="submit">Sign In</button>
        </form>
      @endif
    </section>
  </main>
